import requests
import pandas as pd
import numpy as np
import os
import time
from datetime import datetime, timezone
from dotenv import load_dotenv

start_time = time.time()

# ── Load token from .env file ──────────────────────────────────────────────
load_dotenv()
TOKEN = os.getenv("HS_TOKEN")

if not TOKEN:
    raise ValueError("HS_TOKEN not found in .env file. Please check your .env file.")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# ── Output path ───────────────────────────────────────────────────────────
# Defaults to current directory — override with OUTPUT_PATH env variable
ONEDRIVE_PATH = os.getenv("OUTPUT_PATH", ".")

# ── Helper ─────────────────────────────────────────────────────────────────
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

# ── Step 1: Pull all deals from HubSpot ───────────────────────────────────
print("Pulling deals from HubSpot...")

# Filter deals from 2022-01-01 onwards
START_DATE_MS = int(datetime(2022, 1, 1, tzinfo=timezone.utc).timestamp() * 1000)

url = "https://api.hubapi.com/crm/v3/objects/deals/search"
all_deals = []
after = None

payload = {
    "filterGroups": [{"filters": [
        {"propertyName": "pipeline", "operator": "EQ", "value": os.getenv("HS_PIPELINE_ID")},
        {"propertyName": "salesperson", "operator": "HAS_PROPERTY"},
        {"propertyName": "createdate", "operator": "GTE", "value": str(START_DATE_MS)}
    ]}],
    "properties": [
        "dealname", "dealstage", "amount", "amount_in_home_currency",
        "createdate", "closedate", "days_to_close",
        "hubspot_owner_id", "salesperson",
        "erp_number__c",
        "bu_owner__c", "source__c", "status__c",
        "project_code__c", "project__c", "project_industry__c",
        "project_product_type__c", "dealtype",
        "margin", "standard_margin", "estimated_contract_amount__c",
        "lost_reason__c", "other_lost_reason", "lost_competitor_details__c",
        "closed_won_reason",
        "city__c", "field2__c", "field5__c", "freight_payable_by",
        "disable"
    ],
    "limit": 100
}

while True:
    if after:
        payload["after"] = after
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    results = data.get("results", [])
    all_deals.extend(results)
    print(f"Fetched {len(results)}, total: {len(all_deals)}")
    if "paging" in data:
        after = data["paging"]["next"]["after"]
    else:
        break

# Remove CS0 customer service orders
all_deals = [
    deal for deal in all_deals
    if not deal['properties'].get('dealname', '').startswith('CS0')
]
print(f"After removing CS0 deals: {len(all_deals)}")

# ── Step 2: Build DataFrame ────────────────────────────────────────────────
print("\nBuilding DataFrame...")

records = []
for deal in all_deals:
    row = deal['properties']
    row['deal_id'] = deal['id']
    records.append(row)

df = pd.DataFrame(records)

# Map deal stage IDs to human-readable labels
stage_mapping = {
    '64882091': 'Qualification 1%',
    '64882090': 'Preliminary Communication 10%',
    '64882094': 'Solution Confirmation 20%',
    '64882092': 'Bidding 40%',
    '64831390': 'Business Negotiation 60%',
    '64882095': 'Closing 80%',
    '64882096': 'Close Win',
    '64882097': 'Close Lost'
}
df['dealstage_label'] = df['dealstage'].map(stage_mapping)

# Keep only deals where erp_number__c is null or starts with COR
# Non-COR values indicate data entry errors or legacy records
df = df[
    df['erp_number__c'].isna() |
    df['erp_number__c'].str.startswith('COR', na=True)
]
print(f"After COR filter: {len(df)} rows")

# ── Step 3: Fetch company data ─────────────────────────────────────────────
print("\nFetching company data...")

deal_ids = [deal['id'] for deal in all_deals]
deal_to_company = {}

for batch in chunks(deal_ids, 100):
    url_assoc = "https://api.hubapi.com/crm/v3/associations/deals/companies/batch/read"
    payload_assoc = {"inputs": [{"id": did} for did in batch]}
    response_assoc = requests.post(url_assoc, headers=headers, json=payload_assoc)
    for result in response_assoc.json().get('results', []):
        deal_id = result['from']['id']
        if result.get('to'):
            deal_to_company[deal_id] = result['to'][0]['id']
    time.sleep(0.2)

company_details = {}
company_ids = list(set(deal_to_company.values()))

for batch in chunks(company_ids, 100):
    url_comp_batch = "https://api.hubapi.com/crm/v3/objects/companies/batch/read"
    payload_comp = {
        "inputs": [{"id": cid} for cid in batch],
        "properties": ["name", "erp_number__c"]
    }
    response_comp = requests.post(url_comp_batch, headers=headers, json=payload_comp)
    for result in response_comp.json().get('results', []):
        cid = result['id']
        company_details[cid] = {
            "company_name": result['properties'].get('name'),
            "company_erp": result['properties'].get('erp_number__c')
        }
    time.sleep(0.2)

# Map company details onto df using deal_id as the lookup key
# Note: enumerate-based mapping was avoided due to index drift after CS0/COR filters
deal_id_to_company_details = {}
for deal in all_deals:
    deal_id = deal['id']
    company_id = deal_to_company.get(deal_id)
    if company_id:
        details = company_details.get(company_id, {})
        deal_id_to_company_details[deal_id] = details

df['company_name'] = df['deal_id'].map(lambda x: deal_id_to_company_details.get(x, {}).get('company_name'))
df['company_erp']  = df['deal_id'].map(lambda x: deal_id_to_company_details.get(x, {}).get('company_erp'))

# ── Step 4: Calculate duration ─────────────────────────────────────────────
print("\nCalculating duration...")

now = datetime.now(timezone.utc)

def calculate_duration(row):
    try:
        create = pd.to_datetime(row['createdate'], utc=True)
        if row['dealstage_label'] in ['Close Win', 'Close Lost']:
            end = pd.to_datetime(row['closedate'], utc=True)
        else:
            end = now
        return round((end - create).days, 1)
    except:
        return None

df['duration_days'] = df.apply(calculate_duration, axis=1)

# ── Step 5: Select final columns ──────────────────────────────────────────
df = df[[
    'dealname', 'amount', 'amount_in_home_currency', 'createdate', 'closedate',
    'days_to_close', 'dealstage_label',
    'erp_number__c',
    'company_erp', 'company_name', 'salesperson', 'hubspot_owner_id',
    'bu_owner__c', 'source__c', 'status__c', 'project_code__c',
    'project__c', 'project_industry__c', 'project_product_type__c', 'dealtype',
    'margin', 'standard_margin', 'estimated_contract_amount__c',
    'lost_reason__c', 'other_lost_reason', 'lost_competitor_details__c',
    'closed_won_reason', 'city__c', 'field2__c', 'field5__c',
    'freight_payable_by', 'duration_days', 'disable'
]]

# ── Step 5b: Force numeric types ──────────────────────────────────────────
numeric_cols = ['amount', 'amount_in_home_currency', 'days_to_close',
                'margin', 'standard_margin', 'estimated_contract_amount__c',
                'duration_days']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Treat -1 as same-day close (HubSpot timestamp rounding artifact)
# Negative values beyond -1 are treated as null (data integrity issue)
df['duration_days'] = df['duration_days'].apply(
    lambda x: 0 if x == -1 else (x if pd.notna(x) and x >= 0 else None)
)

# ── Step 5c: Data quality — remove deals with missing createdate ───────────
# createdate is a required HubSpot field; missing values indicate upstream data integrity issues
before = len(df)
df = df[
    df['createdate'].notna() & 
    (df['createdate'] != '') &
    (df['createdate'].astype(str).str.strip() != '')
]
removed = before - len(df)
if removed > 0:
    print(f"Removed {removed} deals with missing createdate (HubSpot data integrity issue)")
# ── Step 6: Filter Close Win with ERP number (for BC join) ────────────────
df_won = df[
    (df['dealstage_label'] == 'Close Win') &
    (df['erp_number__c'].notna()) &
    (df['erp_number__c'] != '')
].copy()
print(f"Close Win with ERP: {len(df_won)} rows")

# ── Step 7: Anonymize for portfolio ───────────────────────────────────────
# All anonymization is applied consistently across both df and df_won
# using shared mapping dictionaries to ensure referential integrity
print("\nAnonymizing data for portfolio...")

np.random.seed(42)

# Anonymize company names → Company_1, Company_2, ...
# Same mapping applied to both df and df_won for consistency
all_companies = df['company_name'].fillna('Unknown').unique()
company_map = {v: f'Company_{i+1}' for i, v in enumerate(all_companies)}
df['company_name'] = df['company_name'].fillna('Unknown').map(company_map)
df_won['company_name'] = df_won['company_name'].fillna('Unknown').map(company_map)

# Anonymize salesperson → SP_01, SP_02, ...
all_salespersons = df['salesperson'].fillna('Unknown').unique()
sp_map = {v: f'SP_{str(i+1).zfill(2)}' for i, v in enumerate(all_salespersons)}
df['salesperson'] = df['salesperson'].fillna('Unknown').map(sp_map)
df_won['salesperson'] = df_won['salesperson'].fillna('Unknown').map(sp_map)

# Anonymize deal names — contain company names and product details
df['dealname'] = 'Deal_' + pd.Series(range(1, len(df)+1), index=df.index).astype(str).str.zfill(6)
df_won['dealname'] = 'Deal_' + pd.Series(range(1, len(df_won)+1), index=df_won.index).astype(str).str.zfill(6)

# Apply random multiplier to amount (1.2, 1.7, or 2.1) to obscure actual revenue
# Multiplier is consistent per row to maintain relative proportions
amount_multipliers = np.random.choice([1.2, 1.7, 2.1], size=len(df))
df['amount'] = (df['amount'] * amount_multipliers).round(2)
df['amount_in_home_currency'] = (df['amount_in_home_currency'] * amount_multipliers).round(2)

won_multipliers = np.random.choice([1.2, 1.7, 2.1], size=len(df_won))
df_won['amount'] = (df_won['amount'] * won_multipliers).round(2)
df_won['amount_in_home_currency'] = (df_won['amount_in_home_currency'] * won_multipliers).round(2)

print(f"Anonymization complete — {len(company_map)} companies, {len(sp_map)} salespersons mapped")

# ── Step 8: Save CSVs to OneDrive ─────────────────────────────────────────
print("\nSaving CSVs to OneDrive...")

deals_path = os.path.join(ONEDRIVE_PATH, 'HS_deals.csv')
won_path   = os.path.join(ONEDRIVE_PATH, 'HS_deals_won.csv')

df.to_csv(deals_path, index=False)
df_won.to_csv(won_path, index=False)

print(f"HS_deals.csv saved:     {len(df)} rows → {deals_path}")
print(f"HS_deals_won.csv saved: {len(df_won)} rows → {won_path}")
print(f"\nDone! Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

elapsed = time.time() - start_time
print(f"\nTotal execution time: {elapsed:.1f} seconds ({elapsed/60:.1f} minutes)")

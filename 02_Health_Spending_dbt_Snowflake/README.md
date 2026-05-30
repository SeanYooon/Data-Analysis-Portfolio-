# Health Spending Visualization – Canada (dbt + Snowflake + Tableau)

**Business Goal:** Build an interactive, per-capita breakdown of Canadian provincial health expenditures (2000–2022) to support public policy analysis and budget planning.

## Tech Stack
- **dbt Cloud** — SQL modeling, testing, and documentation
- **Snowflake** — cloud data warehouse
- **Tableau Public** — interactive dashboards
- **CIHI Open Data** — raw health spending and population data

## Data Pipeline

| Layer | Model | What it does |
|-------|-------|--------------|
| Raw | `HEALTH_SPENDING_RAW` | Source ingestion via `sources.yml` |
| Staging | `stg_health_spending.sql` | Cleans nulls, casts types, calculates `spending_per_capita` and prior-year delta |
| Mart | `mart_health_spending.sql` | Aggregates by province, year, category; computes avg per-capita metrics |
| Tests | `schema.yml` | Automated not-null and uniqueness checks on key fields |

## Key Findings
- Quebec showed a distinct spending growth trajectory compared to BC and Ontario
- Per-capita efficiency gaps between provinces widened significantly post-2015
- Total national health spending crossed a consistent upward inflection post-COVID (2020–2022)

## Screenshots

| Spending by Category & Total Trend | YoY Growth Rate (Canada vs Quebec vs BC) |
|------------------------------------|------------------------------------------|
| ![Dashboard](screenshots/Dashboard_2.png) | ![YoY Growth](screenshots/Sheet_13.png) |

## Links
- **dbt + Snowflake repo:** [github.com/SeanYooon/snowflake_dbt](https://github.com/SeanYooon/snowflake_dbt)
- **Tableau Public dashboard:** [View here](https://public.tableau.com/app/profile/seokhyun.yoon/viz/Book2_17542733788110/Story3)

## Data Source
[CIHI – National Health Expenditure (NHEX) 2024 Full Data Tables](https://www.cihi.ca/sites/default/files/document/nhex-2024-full-data-tables-en.xlsx)

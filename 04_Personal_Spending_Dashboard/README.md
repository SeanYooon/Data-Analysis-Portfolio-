# Personal Spending Dashboard — Power Query + LAMBDA + Dynamic Arrays

A monthly bank-statement tracker built entirely in Excel — no Power BI, no external DB. The goal was to see how far native Excel tools (Power Query, LAMBDA, dynamic arrays) can go for a recurring personal reporting task, without dropping into VBA or a script.

## What it does

- **Ingests** 6 months of raw bank-statement CSVs (`sample_data/`) via **Power Query**, appending them into a single table (`Tx`) and adding computed columns (`Start of Month`, cleaned `Merchant`).
- **Auto-categorizes** every transaction with a reusable `LAMBDA` function:
  ```
  Categorize = LAMBDA(desc,
      XLOOKUP(TRUE, ISNUMBER(SEARCH(tblMap[Keyword], desc)), tblMap[Category], "Uncategorized")
  )
  ```
  This searches each transaction's description against a keyword→category mapping table (`Mapping` sheet) and returns the first match — so adding a new merchant rule is just a new row in the mapping table, not a formula edit.
- **Summarizes** category totals, counts, and share-of-spend using `SORT`/`UNIQUE`/`FILTER` dynamic arrays (no helper columns, no manual drag-fill — the whole `Summarize` sheet recalculates and resizes itself when new months are appended).
- **Flags spend level** per category (`Major` / `Mid` / `Minor`) based on share of total spend, so the biggest drivers surface automatically rather than requiring a manual sort.
- **Dashboard** sheet: pivot tables for spend-by-category and spend-by-month, built directly on top of the `Tx` table so refreshing Power Query refreshes the whole report in one click.

## Why this approach

Most "categorize my spending" tutorials either hardcode `IF` chains per merchant or require a separate script. Keyword-matching through `XLOOKUP` + a `LAMBDA` wrapper means the categorization logic lives in one named function, and the actual rules (which keyword maps to which category) live in a plain table anyone — including non-technical future-me — can edit without touching a formula.

## Sample output (6 months, Mar–Aug)

| Category | Total | Share |
|---|---|---|
| Grocery | $2,978.04 | 29.9% |
| Gas | $1,647.95 | 16.6% |
| Home | $826.86 | 8.3% |
| Dining | $794.75 | 8.0% |
| Cafe | $563.59 | 5.7% |
| Uncategorized | $371.44 | 3.7% |

Grand total across the 6-month window: **$9,954.24**. Only ~3.7% of transactions fell through to "Uncategorized," which is the metric I used to judge whether the mapping table needed more keyword rules.

*Note: the underlying transaction data (merchant names, amounts) has been anonymized before being included in this repo.*

## Files

- `Spending Dashboard.xlsx` — the full workbook (`Data`, `Counttotal`, `Mapping`, `Summarize`, `Dashboard` sheets)
- `sample_data/` — the monthly statement CSVs that feed the Power Query import

## Tech Stack

Excel (Power Query / Get & Transform, LAMBDA, XLOOKUP, dynamic arrays — `UNIQUE`, `FILTER`, `SORT`), PivotTables

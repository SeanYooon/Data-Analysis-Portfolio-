# Credit Risk Prediction & Scoring (Banking-Grade ML Pipeline)

**Business Goal:** Build an end-to-end credit risk pipeline that predicts loan default, maps outputs to a FICO-style 300–850 score, applies the 5 Cs of Credit framework, and quantifies business impact in dollar terms.

## Tech Stack
- **Python** — pandas, numpy, scikit-learn, XGBoost, imbalanced-learn
- **Interpretability** — SHAP (global + local explanations)
- **Visualization** — matplotlib, seaborn
- **Notebook** — Jupyter

## Pipeline Steps

1. **EDA** — outlier detection, missing value imputation, feature-target relationships
2. **Feature Engineering** — debt-to-income ratio, home ownership flags, employment length buckets
3. **Modeling** — XGBoost with `RandomizedSearchCV` tuning; SMOTE for class imbalance
4. **Credit Scoring** — logistic scorecard transformation (PDO=50, base odds=1:9, scale 300–850)
5. **5 Cs Assessment** — Character, Capacity, Capital, Collateral, Conditions integrated into decision logic
6. **Interpretability** — SHAP feature importance for regulatory review
7. **Business Impact Report** — ROC, PR curve, confusion matrix, dollar-value summary

## Results

| Metric | Value |
|--------|-------|
| Hold-out AUC | **0.937** (exceeds industry standard) |
| Default Detection Rate | 76.4% |
| Estimated Loss Prevented | $10.3M |
| Approval Automation Rate | 85% |
| Top Risk Factors | Home ownership, loan grade, DTI, income, loan purpose |

## Regulatory Alignment
- FICO-equivalent scoring (PDO=50, 300–850 scale)
- Basel III, SR 11-7, and Fair Lending (ECOA) principles
- SHAP provides auditable, per-decision explainability

## Screenshots

| Performance Dashboard | SHAP Feature Importance |
|-----------------------|------------------------|
| ![Dashboard](screenshots/credit-dashboard.png) | ![SHAP](screenshots/credit-shap.png) |

## Files
- `credit_risk.ipynb` — full end-to-end notebook

## Data Source
[Kaggle – Credit Risk Dataset](https://www.kaggle.com/datasets/laotse/credit-risk-dataset)

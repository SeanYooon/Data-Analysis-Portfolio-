# Seokhyun Yoon – Data Analyst Portfolio

## 👋 About Me

Hello, I'm Seokhyun Yoon — a Statistics graduate from Simon Fraser University with a strong foundation in data analysis, machine learning, and business intelligence tools.

I specialize in applying predictive modeling, time series forecasting, classification algorithms, and dashboarding to solve real-world business challenges in areas such as customer retention, credit risk, digital marketing ROI, and geospatial insights.

I work primarily with **Python, R, SQL, Power BI, Tableau**, and version control tools like Git. My goal is to transform complex data into actionable insights and data products that help stakeholders make better decisions.

This repository showcases selected projects that demonstrate my technical proficiency, business thinking, and ability to deliver data-driven solutions.

✍️ [View My Resume (PDF)](https://github.com/SeanYooon/Data-Analysis-Portfolio-/blob/600ea4af8f841bf852fe868ec03f4e31772f46f97/Sean%20Resume.pdf)
🔗 [Visit My LinkedIn](https://www.linkedin.com/in/seokhyun-yoon-241a61104/)

---

## 📁 Table of Contents

* [👋 About Me](#-about-me)
* [📊 Project Portfolio](#-project-portfolio)

  * [Credit Risk Prediction & Scoring](#credit-risk-prediction--scoring)
  * [Customer Churn Prediction Dashboard](#customer-churn-prediction-dashboard)
  * [Marketing Campaign ROAS Optimization](#marketing-campaign-roas-optimization)
  * [SpaceX Falcon 9 Landing Prediction](#spacex-falcon-9-landing-prediction)
  * [Housing Price Prediction](#housing-price-prediction)
  * [Rainfall Forecasting (Time Series)](#rainfall-forecasting-time-series)
  * [Police Complaints Prediction](#police-complaints-prediction)
  * [Health Spending Visualization (Canada)](#health-spending-visualization-canada)
  * [Insurance Cost Analysis (Excel)](#insurance-cost-analysis-excel)

---

## 📊 Project Portfolio
---

###  Credit Risk Prediction (Loan Default Classification)

**Business Goal:** Predict the likelihood of loan default to assist lenders in minimizing financial risk and improving credit approval accuracy.

* **Tech Stack:** Python, Pandas, Scikit-learn, PyTorch, SMOTE, Matplotlib, Seaborn  
* **Key Actions:**
  * Cleaned and encoded borrower data (categorical + numerical features)
  * Engineered features like DTI ratio and employment length groups
  * Applied SMOTE to resolve class imbalance (default vs non-default)
  * Trained and compared classifiers (Logistic Regression, Random Forest, PyTorch Neural Network)
  * Visualized results using confusion matrices and SHAP interpretability tools

* **Results:**  
  * PyTorch model achieved ~85% classification accuracy  
  * Balanced recall and precision across both classes after SMOTE  
  * Identified high DTI and low income as key predictors of default  
  * SHAP analysis supported explainable predictions for stakeholders

* **Visuals:**


| Performance Dashboard                             | Model Interpretability          |
|-------------------------------------------------------|--------------------------------------------|
|![*ROC, Debt-to-Income by Default, Precision-Recall, Confusion Matrix*](images/credit-dashboard.png)    | ![*Top 5 SHAP feature importances (housing status, loan grade, DTI, etc.)*](images/credit-shap.png) |

* **Files:**  
- [`credit_risk.ipynb`](/files/credit_risk.ipynb) – full notebook
---
###  Customer Churn Prediction Dashboard

**Business Goal:** Predict telecom customer churn and deliver actionable BI insights to help reduce retention risk and optimize decision-making.

* **Tech Stack:** Python, Pandas, Scikit-learn, PyTorch, SMOTE, Power BI, SQL  
* **Key Actions:**
  * Cleaned Telco dataset and performed feature engineering (e.g., contract length, charges per tenure)
  * Designed OLAP-style schema with fact and dimension tables for slicing by customer segments
  * Trained a churn classification model using PyTorch with SMOTE to balance the classes
  * Evaluated model using accuracy, confusion matrix, and classification report
  * Built Power BI dashboard to visualize KPIs, churn heatmap, trends, and customer segments

* **Results:**  
  * Achieved over 80% accuracy in churn classification with balanced sensitivity  
  * Identified key churn drivers (monthly charges, contract type, tenure)  
  * Delivered an interactive dashboard for decision-makers to explore churn by segment  
  * Enabled early detection of at-risk customers and data-driven intervention strategies

* **Visuals:**

| KPI: Churn Rate | Churn by Internet Service |
|----------------|---------------------------|
| ![KPI Churn](images/telco5.png) | ![Internet Type](images/telco2.png) |

* **Files:** 
- [`churn_analysis.ipynb`](files/Churn.ipynb) – Notebook  
- [`cleaned_telco_churn.csv`](files/cleaned_telco_churn.csv) – Dataset
- [`Original_churn_data.csv`](files/WA_Fn-UseC_-Telco-Customer-Churn_(1).csv) – Dataset 
---
###  Ad Campaign ROAS Analysis

**Business Goal:** Analyze and compare the Return on Ad Spend (ROAS) across multiple ad platforms to identify the most cost-effective marketing channels.

* **Tech Stack:** Excel, Tableau, Power BI, SQL (Optional upgrade path: replicate using Python & SQL)  
* **Key Actions:**
  * Collected and organized campaign data across Facebook, Google, and YouTube ads
  * Calculated ROAS, CTR, CPC, and CPM metrics for each campaign and platform
  * Created custom visuals to compare KPIs, cost distribution, and performance trends
  * Delivered dashboard and presentation highlighting the highest and lowest performing channels
  * Suggested reallocation strategies for future ad budgets based on findings

* **Results:**  
  * Identified Google Ads as highest ROAS (~3.5x), while YouTube underperformed (<1x)  
  * Found a clear inverse relationship between ad cost and effectiveness on certain platforms  
  * Supported marketing team in shifting budget to high-ROI channels and pausing weak performers

* **Visuals:**

| Model Analysis                            | Actual vs Predicted           |
|-------------------------------------------------------|--------------------------------------------|
|![Actual vs Predicted](images/roas_model_analysis.png)    | ![Feature Importance](images/actual_vs_predicted_roas.png) |

* **Files:** 
- [`churn_analysis.ipynb`](files/Churn.ipynb) – Notebook  
- [`cleaned_telco_churn.csv`](files/cleaned_telco_churn.csv) – Dataset
- [`Original_churn_data.csv`](files/WA_Fn-UseC_-Telco-Customer-Churn_(1).csv) – Dataset 
---

###  SpaceX Falcon 9 Landing Prediction

**Business Goal:** Predict booster landing success to support mission planning and reduce launch failure risks.

* **Tech Stack:** Python, Pandas, Scikit-learn, Plotly Dash, Folium, SQL  
* **Key Actions:**
  * Pulled and cleaned SpaceX API data; added features via scraping (e.g., booster version)
  * Conducted EDA with SQL, time series, and categorical visualizations
  * Built interactive dashboard (Dash) and geographic map (Folium)
  * Trained and compared classifiers (Logistic Regression, SVM, Decision Tree)

* **Results:**  
  * Found strong correlations between orbit type and landing success  
  * Identified an increasing success trend with higher flight numbers  
  * Delivered an interactive tool for launch analysis and planning

* **Visuals:**

| Interactive Launch Map (Folium)                         | Model Accuracy Chart                          |
|---------------------------------------------------------|-----------------------------------------------|
| ![Folium Map](images/spacex_map.jpg)                    | ![Model Accuracy](images/spacex_accuracy.jpg) |

* **Files:**  

- [`SpaceX_Machine_Learning_Prediction.ipynb`](files/SpaceX_Machine_Learning_Prediction_Part_5.jupyterlite.ipynb) – full Jupyter notebook  
- [`falcon9.pdf`](files/spacex-final.pdf) – final PDF summary
---
### Housing Price Prediction

**Business Goal:** Predict home prices from large-scale Connecticut housing data.

* **Tech Stack:** R, XGBoost, glmnet, tidyverse
* **Key Actions:**

  * Cleaned and transformed 995K+ sales records
  * Tuned XGBoost model with interaction terms and log scaling
* **Results:**

  * RMSE = 1.15; top features include location and assessed value

* **Visuals:**
  
| Actual vs Predicted                               | Feature Importance          |
|-------------------------------------------------------|--------------------------------------------|
|![Actual vs Predicted](images/housing-importance.png)   | ![Feature Importance](images/housing-log.png) |

---
###  Rainfall Forecasting (Time Series)

**Business Goal:**  
Forecast monthly rainfall in Perth, Australia to support weather planning and hydrology management using long-term seasonal patterns.

* **Tech Stack:**  
  R, `forecast`, `tseries`, `ggplot2`, Box-Jenkins Methodology

* **Key Actions:**  
  * Loaded and cleaned 106 months of historical rainfall data  
  * Conducted stationarity checks and seasonal decomposition  
  * Performed grid search to optimize SARIMA parameters based on AIC  
  * Trained SARIMA(1,0,0)(0,1,1)[12] model to forecast 14 future months  
  * Compared against a dynamic regression model with covariates  
  * Validated forecasts against actual rainfall from BOM (Australia)

* **Results:**  
  * Achieved >10% improvement in accuracy after model refinement  
  * Detected strong annual seasonality in rainfall patterns  
  * Delivered an interpretable model with clear confidence intervals  
  * Highlighted SARIMA as effective for mid-term weather forecasting

* **Visuals:**
 
| Forecast Plot                                | Residual ACF          |
|-------------------------------------------------------|--------------------------------------------|
|![Forecast Plot](images/Rplot.png) | ![Residual ACF](images/rainfallacf.png) |

* **Files:**
  
- [`Rainfall.Rmd`](rainfall_forecasting.Rmd) – full notebook
- [`IDCJAC0009_009021_1800_Data.csv`](data/rainfall.csv) – historical rainfall data  
- [`images/rainfall_forecast.pdf`](images/rainfall_forecast.pdf) – forecast plot  
- [`images/residual_acf.pdf`](images/residual_acf.pdf) – residual autocorrelation chart
- [`Rainfall_Report.pdf`](files/485_Project_Report_Official.pdf) - Rainfall report 
---
### Police Complaints Prediction

**Business Goal:** Predict misconduct complaints among officers using historical data.

* **Tech Stack:** R, XGBoost, Random Forest, ROC curves
* **Key Actions:**

  * Modeled likelihood of complaints from demographic/service history
  * Addressed fairness/ethics concerns in model usage
* **Results:** High-AUC classifiers with ethical lens
---
###  Health Spending Visualization (Canada)

**Business Goal:**  
Provide an interactive breakdown of per-capita and categorical health expenditures across Canadian provinces to support public policy evaluation and stakeholder insight.

* **Tech Stack:**  
  Tableau Public, Excel, CIHI Open Data (Canadian Institute for Health Information)

* **Key Actions:**  
  * Cleaned and joined provincial health spending and population datasets (2000–2022)  
  * Created calculated fields for per-capita metrics and YoY percentage growth  
  * Designed a multi-page Tableau dashboard with province/category/time filters  
  * Published dashboard to [Tableau Public](https://public.tableau.com/app/profile/seokhyun.yoon/viz/Book2_17542733788110/Story3)

* **Results:**  
  * Highlighted national and provincial healthcare spending trends over 20+ years  
  * Visualized Quebec’s divergent YoY growth and per-capita efficiency  
  * Dashboard used as a stakeholder tool for comparing hospital, drugs, and physician costs  
  * Improved accessibility of public health data through a visual-first interface

* **Visuals:**

| Stacked Bar + Dot Line – Spending by Category and Total Trend                              | Line Chart – YoY Growth Rate (Canada vs Quebec vs BC)         |
|-------------------------------------------------------|--------------------------------------------|
|![Forecast Plot](images/Dashboard_2.png) | ![Residual ACF](images/Sheet_13.png) |

---
### Insurance Cost Analysis (Excel)

**Business Goal:** Simulate group benefits cost modeling for Sun Life-like scenarios.

* **Tech Stack:** Excel, Pivot Tables, VBA
* **Key Actions:**

  * Built age-tiered risk model using Excel formulas and macros
  * Automated premium segmentation and risk profiling
* **Results:** Dashboard visualizing smoker cost impact, family size premiums, and risk categories

---

## 🎓 Education

**Simon Fraser University** — Burnaby, BC
Bachelor of Science in Statistics
*May 2018 – December 2023*

---

## 📜 Certificates

* [IBM Data Science Professional Certificate](https://www.coursera.org/account/accomplishments/specialization/XQD6FNV9Q5FB) (Dec 2023)
* [Deep Learning Specialization – DeepLearning.AI](https://coursera.org/share/HROP8FKWDLCK) (Oct 2024)
* [Tableau for Data Analytics – LinkedIn Learning](https://www.linkedin.com/learning/certificates/814d91fd0c6ab19bb16c9d29fd23fb3a7915ad908637ed0b5ba19f5684ac1dc5) (Jan 2023)

---

## 📬 Contact

* 📧 Email: [seokhyun.sean.yoon@gmail.com](mailto:seokhyun.sean.yoon@gmail.com)
* 💼 LinkedIn: [@Seokhyun\_Yoon](https://www.linkedin.com/in/seokhyun-yoon-241a61104/)

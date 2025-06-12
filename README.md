# Seokhyun Yoon - Data Analyst Portfolio

## 👋 About Me

Hello, I'm Seokhyun Yoon — a Statistics graduate from Simon Fraser University with a strong foundation in data analysis, machine learning, and business intelligence tools.

I’ve developed hands-on projects applying predictive modeling, time series analysis, and classification algorithms to real-world problems such as rainfall forecasting, housing price prediction, and rocket landing success rates.

I work primarily with **Python, R, SQL, Power BI, Tableau**, and version control tools like Git. I enjoy simplifying complex data into actionable insights and visual stories that help people make better decisions.

This repository showcases selected projects that reflect my technical skill set and my ability to turn raw data into practical outcomes.  
📄 [View My Resume (PDF)]([Sean Resume.pdf](https://github.com/SeanYooon/Data-Analysis-Portfolio-/blob/600ea4aff841bf852fe868ec03f4e31772f46f97/Sean%20Resume.pdf))  
🔗 [Visit My LinkedIn](https://www.linkedin.com/in/seokhyun-yoon-241a61104/)

Let’s connect!

---

## 📁 Table of Contents

- [About](#about)
- [Portfolio Projects](#portfolio-projects)
  - Python
    - [SpaceX Falcon 9 Landing Prediction](#spacex-falcon-9-landing-prediction)
  - R
    - [Housing Price Prediction](#housing-price-prediction)
    - [Police Complaints Prediction](#police-complaints-prediction)
    - [Rainfall Time Series Forecasting](#rainfall-time-series-forecasting)
- [Education](#education)
- [Certificates](#certificates)
- [Contact](#contacts)

---

## 📊 Portfolio Projects

Here are some of the projects I've completed, along with brief descriptions of the tools, goals, and results.

---

# 🚀 SpaceX Falcon 9 Landing Prediction – Classification + Mapping

## 📊 Project Overview
Predicted the landing success of SpaceX Falcon 9 first-stage boosters using a classification model. Combined machine learning with geospatial visualizations and API-sourced launch data to explore how mission factors influence outcomes.

---

## 🔧 Tools & Techniques
Python, Pandas, Scikit-learn, Folium, Plotly, SpaceX API  
Classification (Logistic Regression, SVM, Random Forest), Feature Engineering, API Integration

---

## 🧠 Key Steps
- Scraped and queried launch data via the SpaceX REST API  
- Cleaned and transformed features (e.g., payload mass, orbit, site ID)  
- Engineered new features like payload class and binary landing outcome  
- Built and compared classification models: Logistic Regression, SVM, Random Forest  
- Evaluated models using accuracy, precision, confusion matrix  
- Created an interactive landing site map using Folium

---

## ✅ Results
- **Best model:** Random Forest Classifier (Accuracy ~87%)  
- **Top predictive features:** Launch Site, Payload Mass, Orbit  
- Created interactive dashboard to visualize outcomes by location

---

## 📊 Visuals

### 📍 Landing Outcome Map (Folium)
![Landing Map](images/falcon9_map.png)

### 📊 Feature Importance
![Feature Importance](images/falcon9_feature_importance.png)

---

## 📂 Files
- [`SpaceX_Machine_Learning_Prediction_Part_5.jupyterlite-2.ipynb`](SpaceX_Machine_Learning_Prediction_Part_5.jupyterlite-2.ipynb) – full Jupyter notebook  
- [`images/falcon9_map.png`](images/falcon9_map.png) – launch site outcome map  
- [`images/falcon9_feature_importance.png`](images/falcon9_feature_importance.png) – model insights  
- [`falcon9.pdf`](falcon9.pdf) – final PDF summary

---

# 🏠 Housing Price Prediction – Connecticut Home Sales (2019–2020)

## 📊 Project Overview
Predicted residential housing prices in Connecticut using a dataset of 995,000+ property sales. Built a regression model using XGBoost, with focus on data cleaning, feature engineering, and model tuning.

## 🔧 Tools & Technologies
R, XGBoost, tidyverse, glmnet, ranger, LightGBM, data.table

## 🧠 Key Steps
- Cleaned and prepared ~1M records from 2019–2020
- Created new time-based and interaction features
- Handled missing values through median/monthly imputation
- Applied log transformation to reduce skew
- Tuned XGBoost with randomized search + early stopping

## 📈 Results
- **Validation RMSE:** 1.15  
- **Validation R²:** 0.26  
- Top features: Assessed value, Town (Greenwich), interaction terms

## 📊 Visuals
![Actual vs Predicted](images/actual_vs_predicted.png)  
![Feature Importance](images/feature_importance.png)

## 📂 Files
- `Housing-price-prediction.Rmd` – full model notebook
- `data/` – cleaned CSVs
- `images/` – result plots
---

### 🚓 Police Complaints Prediction

**Code:**  
- [`Final_Version.R`](https://github.com/jasondang01/440module2-jason-tyler-sean/blob/main/Final_Version.R)

**Goal:** Predict which CPD officers would receive complaints in 2015–2016 using data from 2000–2014.

**Description:** Modeled officer misconduct likelihood based on salary, prior complaints, and service data. Explored fairness and ethical data analysis.

**Skills:** Data cleaning, feature engineering, classification, ROC analysis  
**Tech Stack:** R, ggplot2, dplyr, tidyr, randomForest, XGBoost, pROC

**Results:** Built accurate classifiers using Random Forest and XGBoost. Evaluated models with AUC and ROC metrics.

---

# 🌧️ Rainfall Forecasting – Time Series Analysis (Perth, Australia)

## 📊 Project Overview
Forecasted monthly rainfall totals in Perth using a SARIMA model trained on 106 months of historical weather data. Applied time series modeling techniques (Box-Jenkins methodology) to capture seasonality and make future projections.

---

## 🔧 Tools & Techniques
- R, `forecast`, `tseries`, `ggplot2`
- SARIMA modeling
- Box-Jenkins methodology
- Residual diagnostics (ACF/PACF)
- Forecast validation against real data

---

## 🧠 Key Steps
- Loaded and cleaned 106 months of historical rainfall data
- Conducted stationarity tests and seasonality checks
- Ran a grid search over SARIMA configurations with AIC optimization
- Selected SARIMA(1,0,0)x(0,1,1)[12] based on lowest AIC
- Forecasted 14 future months (months 107–120)
- Validated predictions against real airport rainfall data
- Sourced rainfall data from the Australian Bureau of Meteorology (BOM) official dataset
- Compared SARIMA model against a dynamic regression benchmark with external covariates

---

## 📈 Results
- **Model used:** SARIMA(1,0,0)x(0,1,1)[12]
- **Forecasted range:** Months 107–120
- **RMSE:** 1.095  
- **MAE:** 0.863  
- **95% CI coverage:** Forecasts closely followed actual values

---

## 📊 Visuals
![Forecast Plot](images/rainfall_forecast.pdf)
![Residual ACF](images/rainfallacf.pdf)

---

## 📂 Files
- [`Rainfall.Rmd`](rainfall_forecasting.Rmd) – full notebook
- [`IDCJAC0009_009021_1800_Data.csv`](data/rainfall.csv) – historical rainfall data  
- [`images/rainfall_forecast.pdf`](images/rainfall_forecast.pdf) – forecast plot  
- [`images/residual_acf.pdf`](images/residual_acf.pdf) – residual autocorrelation chart
- - [`Rainfall_Report.pdf`](files/485 Project Report Official.pdf)
---

## 🎓 Education

**Simon Fraser University** — Burnaby, BC  
Bachelor of Science in Statistics  
*May 2018 – December 2023*

---

## 📜 Certificates

While real projects are the best proof of skills, I’ve also completed these certifications:

- [IBM Data Science Professional Certificate](https://www.coursera.org/account/accomplishments/specialization/XQD6FNV9Q5FB) (Dec 2023)
- [Deep Learning Specialization – DeepLearning.AI](https://coursera.org/share/HROP8FKWDLCK) (Oct 2024)  
- [Tableau for Data Analytics – LinkedIn Learning](https://www.linkedin.com/learning/certificates/814d91fd0c6ab19bb16c9d29fd23fb3a7915ad908637ed0b5ba19f5684ac1dc5) (Jan 2023)

---

## 📬 Contact

- 📧 Email: [seokhyun.sean.yoon@gmail.com](mailto:seokhyun.sean.yoon@gmail.com)  
- 💼 LinkedIn: [@Seokhyun_Yoon](https://www.linkedin.com/in/seokhyun-yoon-241a61104/)

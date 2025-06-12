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

### 🚀 SpaceX Falcon 9 Landing Prediction

**Code:**  
- [`Study Notebook`](https://github.com/DoubleOne7/coursera/blob/main/coursera-study-project.ipynb)  
- [`Folium Interactive Map`](https://nbviewer.org/github/DoubleOne7/coursera/blob/main/lab_jupyter_launch_site_location%20%282%29.ipynb)  

**Report:**  
- [`spacex-final.pdf`](https://github.com/DoubleOne7/coursera/blob/main/spacex-final.pdf)

**Goal:** Predict whether the first stage of the Falcon 9 rocket will successfully land after launch.

**Description:** Applied machine learning to model landing outcomes for SpaceX rockets. This project aimed to help reduce costs and improve decision-making in commercial space launches.

**Skills:** API requests, data cleaning, mapping, visualization, correlation analysis  
**Tech Stack:** Python, Pandas, NumPy, Seaborn, Matplotlib, SQL, BeautifulSoup, Folium

**Results:** Built a robust ML model using classification techniques that accurately predicted landing outcomes.

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
![Residual ACF](images/residual_acf.png)

---

## 📂 Files
- [`rainfall_forecasting.Rmd`](rainfall_forecasting.Rmd) – full notebook
- [`data/rainfall.csv`](data/rainfall.csv) – historical rainfall data  
- [`images/rainfall_forecast.png`](images/rainfall_forecast.png) – forecast plot  
- [`images/residual_acf.png`](images/residual_acf.png) – residual autocorrelation chart
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

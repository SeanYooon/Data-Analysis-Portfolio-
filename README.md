# Seokhyun Yoon - Data Analyst Portfolio
## About Me
Hello, I'm Seokhyun! With a Bachelor of Science in Statistics and a certificate in IBM Data Science, I possess a strong foundation in statistical analysis and a passion for leveraging data to derive meaningful insights. My academic journey has equipped me with extensive knowledge in machine learning algorithms, data visualization, and predictive modeling.

I am deeply fascinated by the potential of data to drive decision-making and problem-solving across various domains. Whether it's exploring precipitation patterns or building predictive models for housing prices, I thrive on the challenge of unraveling complex datasets to extract actionable insights.

Outside of academics and work, I am committed to continuous learning and stay updated on the latest advancements in data analytics tools and techniques. I am eager to contribute my technical expertise and analytical prowess to projects that drive innovation and create tangible impact.

You can view my resume [pdf](https://github.com/DoubleOne7/Data-Analysis-Portfolio-/blob/main/Seokhyun%20Yoon%20resume.pdf). 

This repository to showcase of my skills, featuring projects that demonstrate my proficiency in data analysis, statistical modeling, and problem-solving. I am excited to embark on my journey as a data analyst and eager to tackle new challenges in the ever-evolving field of data science.


## Table of Contents
- [About](https://github.com/DoubleOne7/Data-Analysis-Portfolio-/blob/main/README.md#about)
- [Portfolio Projects](https://github.com/DoubleOne7/Data-Analysis-Portfolio-/blob/main/README.md#portfolio-projects)
  - Python
    - [SpaceX Falcon 9 first stage Landing Prediction](https://github.com/DoubleOne7/Data-Analysis-Portfolio-#SpaceX-Falcon-9-first-stage-Landing-Prediction)
  - R
    - [Housing price prediction](https://github.com/DoubleOne7/Data-Analysis-Portfolio-#legendary-pok%C3%A9mon-analysis)
    - [Police complaints prediction](https://github.com/DoubleOne7/Data-Analysis-Portfolio-#Police-complaints-prediction)
    - [Time Series Analysis of Rainfall Data](https://github.com/DoubleOne7/Data-Analysis-Portfolio-#Time-Series-Analysis-of-Rainfall-Data)

- [Education](https://github.com/DoubleOne7/Data-Analysis-Portfolio-/blob/main/README.md#education)  
- [Certificates](https://github.com/DoubleOne7/Data-Analysis-Portfolio-/blob/main/README.md#certificates)
- [Contact](https://github.com/DoubleOne7/Data-Analysis-Portfolio-/blob/main/README.md#contacts)
## Portfolio Projects
In this section I will list data analytics projects briefly describing the technology stack used to solve cases.

### SpaceX Falcon 9 first stage Landing Prediction
**Code:** 
- [Coursera Study Project Notebook](https://github.com/DoubleOne7/coursera/blob/main/coursera-study-project.ipynb)
- [Folium Interactive Map Notebook](https://nbviewer.org/github/DoubleOne7/coursera/blob/main/lab_jupyter_launch_site_location%20%282%29.ipynb)

**Report**
- [`spacex-final.pdf`](https://github.com/DoubleOne7/coursera/blob/main/spacex-final.pdf)

**Goal:** Develop machine learning algorithms for predicting the successful landing of the Falcon 9 first stage.

**Description:** This capstone project focuses on leveraging machine learning techniques to predict whether the first stage of the Falcon 9 rocket will successfully land after launch. The successful landing of the first stage is crucial for reducing launch expenses and determining the overall cost-effectiveness of space missions. By accurately predicting landing outcomes, this project aims to provide valuable insights into launch cost estimation, influencing decision-making processes for companies entering the competitive space exploration market.

**Skills:** request api, data cleaning, Interactive map, data wrangling, data visualization, data analysis, correlation matrix

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib, SQL, bs4, Folium

**Results:** Through Python functions, comprehensive data analysis, visualization, and machine learning model development were conducted, resulting in a robust predictive model capable of accurately forecasting Falcon 9 first stage landing outcomes.


###  Housing price prediction

**Goal:** To make a best prediciton for the close test housing data set.

**Code:** 
- [`Housing-price-prediction.Rmd`](https://github.com/DoubleOne7/Housing-prediciton-project/blob/main/Housing-price-prediction.Rmd)

**Description:** This project focuses on leveraging machine learning techniques to predict the sale price (in USD) of residential properties in Connecticut, based on sales data encompassing 995,644 properties sold between 2019 and 2020. The dataset includes properties sold for less than $10,000,000. The training set constitutes 20% of the data, while the private leaderboard comprises 50% of the testing set. Covariates such as List_Year indicate the year of property listing, and Date_Recorded denotes the completion date of the sale. Additionally, the Address covariate contains the street name of the property, with street numbers suppressed.

**Skills:** data cleaning, data analysis, data visualization, data imputation, meachine learning

**Technology:** R, tidyverse, glmnet, Xgboost

**Results:** Utilizing advanced machine learning technique, XGBoost in R, we can create a sophisticated predictive model for housing prices. By incorporating feature engineering, hyperparameter tuning, and ensemble methods, we can enhance the model's accuracy and robustness, providing accurate predictions for housing prices with high precision and flair. 


### Police complaints prediction 

**Code:** 
- [`Police-complaints-prediction.R`](https://github.com/jasondang01/440module2-jason-tyler-sean/blob/main/Final_Version.R)

**Description:** Police violence is a serious concern in North America and throughout the world. The Chicago Police Department (CPD) has been criticized for their potentially excessive use of deadly force. Regarding CPD, a particularly hard time in Chicago has been identified between 2000 and 2016, and after extensive FOIA (Freedom of Information Act) requests, information about CPD during this period (including formal complaints) are now in the public domain. In this module, you will predict which CPD officers had complaints filed against them in 2015 and 2016, given information from 2000 to 2014 involving prior complaints, salary, covariates, and awards.

**Skills:** data cleaning, data imputation, feature engineering, machine learning, AUC, ROC. 

**Technology:** R, ggplot2, dplyr, tidyr, random forest, Xgboost, pRoc

**Results:** Utilizing advanced machine learning techniques like random forest and XGBoost in R, we can create a sophisticated predictive model for housing prices. By incorporating feature engineering, hyperparameter tuning, and ensemble methods, we can enhance the model's accuracy and robustness, providing accurate predictions for housing prices with high precision. By computing the Area Under the Curve (AUC) and Receiver Operating Characteristic (ROC) metrics, we validate the model's performance, showcasing its ability to accurately predict police complaint occurrences with remarkable precision. 

### Time Series Analysis of Rainfall Data

**Goal:**  To analyze historical rainfall data for Perth, Australia, using time series analysis techniques

**Code:** 
- [`Time-Series-Analysis-of-Rainfall-Data.Rmd`](https://github.com/bba32/stat485/blob/main/Rainfall%20Final.Rmd)

**report** 
- [`485 Project Report Official.pdf`](https://github.com/DoubleOne7/Data-Analysis-Portfolio-/blob/main/485%20Project%20Report%20Official.pdf)

**Description:** This project involves the analysis of historical rainfall data for Perth, Australia, using time series analysis techniques. The main objectives are to identify patterns and trends in monthly average rainfall, select the most suitable ARIMA model for forecasting future rainfall, generate a 12-month precipitation forecast, and validate the forecast accuracy against actual data. By leveraging time series analysis, the project aims to provide valuable insights into Perth's rainfall patterns and develop a reliable forecasting model to support decision-making in various sectors such as water resource management and urban planning.

**Skills:** data cleaning, data analysis, data visualization, time series analysis, model selection, forecasting

**Technology:** dplyr, tidyr, TSA, forecast. 

**Results:** Utilizing advanced time series analysis methods such as ARIMA modeling in R, we can develop a sophisticated forecasting model for monthly rainfall in Perth. By leveraging techniques like Box-Jenkins method and dynamics modeling, along with careful model selection and validation, we ensure the accuracy and reliability of our forecasts. Furthermore, by computing evaluation metrics like Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE), we validate the model's performance and demonstrate its capability to provide precise forecasts of rainfall patterns in the region.

## Education
Simon Fraser University, Burnaby: 
Bachelor of Science - Statistics,
May 2018 - Dec 2023

## Certificates
The best way to showcase skills is by doing and sharing your job done but sometimes certificates appear to be as an indirect result. Here's a list of the ones I have (in reverse-chronological order, with the date of completion in brackets):
- [IBM Data Science Professional](https://www.coursera.org/account/accomplishments/specialization/XQD6FNV9Q5FB) (Dec 2023) (Coursera - IBM)
- [Tableau](https://www.linkedin.com/learning/certificates/814d91fd0c6ab19bb16c9d29fd23fb3a7915ad908637ed0b5ba19f5684ac1dc5) (Jan 2023) (Linkedin Learning)

## Contacts
- LinkedIn: [@Seokhyun_Yoon](https://www.linkedin.com/in/seokhyun-yoon-241a61104/)
- Email: 96ssamba@gmail.com

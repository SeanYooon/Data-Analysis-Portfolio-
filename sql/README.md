# Customer Churn Analysis - SQL Star Schema Implementation

## Overview
This project demonstrates data warehouse design principles using a star schema 
approach for customer churn analysis, directly applicable to healthcare patient 
retention and population health analytics.

## Star Schema Design

### Fact Table: `customer_churn_facts`
- **Grain:** One row per customer with churn outcome
- **Measures:** Monthly charges, total charges, tenure months, churn flag
- **Keys
- `dim_customer_demographics` - Age, gender, partner status, dependents
- `dim_service_details` - Internet service, phone service, tech support
- `dim_contract_info` - Contract type, payment method, billing preferences
- `dim_time` - Tenure groupings, contract start periods

## Healthcare Analytics Application
This star schema approach directly applies to:
- Patient retention analysis across service lines
- Population health KPI reporting  
- Clinical outcome tracking by demographics
- Healthcare utilization pattern analysis

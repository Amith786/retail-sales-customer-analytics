# Retail Sales & Customer Analytics Using Python

## 📊 Project Overview

This repository contains an end-to-end **Business Analytics project** focused on analysing retail sales and customer transaction data using Python.

The project is being developed as part of the **Junior Data Analyst – Business Analytics with Python internship at YuvaIntern**. It follows a structured six-week analytics workflow, progressing from business strategy and data preparation to visualization, statistical analysis, predictive modeling, dashboard development, and final business recommendations.

The project demonstrates a complete data analytics workflow, transforming raw transactional data into meaningful insights that can support data-driven business decision-making.

---

## 🎯 Project Objectives

The project aims to transform raw retail transaction data into meaningful business insights by exploring key areas such as:

- 📈 Sales performance and revenue trends
- 🛍️ Product performance and purchasing patterns
- 👥 Customer behaviour and transaction value
- 🌍 Geographic sales patterns
- 🧹 Data quality, cleaning, and transformation
- 📊 Statistical relationships and hypothesis testing
- 🤖 Predictive modeling and sales forecasting
- 💡 Data-driven business planning and recommendations

---

## 📂 Dataset

The project uses the **Online Retail dataset** from the UCI Machine Learning Repository. The dataset contains transactional information related to invoices, products, quantities, unit prices, customers, transaction dates, and countries.

During the project, the raw dataset is cleaned and transformed to create additional analytical features, including:

- `TotalSales`
- Year and month information
- Day and day-of-week variables
- Transaction and sales-related analytical features

> **Note:** The original dataset is publicly available from the UCI Machine Learning Repository. Large raw data files may not be stored directly in this repository.

---

## 🛠️ Tools and Technologies

- **Python** – Core programming language
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computing
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **SciPy** – Statistical hypothesis testing
- **Scikit-learn** – Machine learning and predictive modeling
- **Jupyter Notebook** – Interactive analysis and documentation
- **Streamlit** – Dashboard development

---

## 🔍 Key Analysis Completed

### 🧹 Data Wrangling and Cleaning

The raw retail dataset was assessed and prepared for analysis by addressing data quality issues, examining duplicate records, handling missing values, transforming data types, and creating useful analytical features.

### 📊 Data Visualization and Reporting

Visualizations were created to explore:

- Monthly sales trends
- Top-performing products
- Country-wise revenue
- Day-of-week sales patterns
- Transaction sales distributions

These visual analyses helped convert transactional data into understandable business insights.

### 📈 Statistical Analysis

Statistical techniques were applied to investigate patterns and relationships within the dataset, including:

- Descriptive statistical analysis
- Correlation analysis
- Independent samples t-test
- Chi-square test of independence

The analysis identified statistically significant differences in sales behavior across different transaction groups.

### 🤖 Predictive Modeling

A **Linear Regression model** was developed as a baseline approach for predicting daily sales revenue using time and calendar-related features.

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score
- Actual vs. Predicted Sales visualization
- Residual analysis

The evaluation highlighted the limitations of a simple linear model in capturing sudden fluctuations in retail sales, providing a foundation for future model improvement.

---

## 🗺️ Project Roadmap

| Week | Task | Status |
|------|------|--------|
| Week 1 | Business Analytics Strategy Planning | ✅ Completed |
| Week 2 | Data Wrangling and Cleaning with Python | ✅ Completed |
| Week 3 | Data Visualization and Reporting | ✅ Completed |
| Week 4 | Statistical Analysis and Predictive Modeling | ✅ Completed |
| Week 5 | Dashboard Development and Reporting | ⏳ Upcoming |
| Week 6 | Comprehensive Business Analytics Evaluation | ⏳ Upcoming |

---

## 📁 Repository Structure

```text
retail-sales-customer-analytics/
│
├── README.md
├── notebooks/          # Python analysis notebooks
├── reports/            # Weekly internship reports
├── data/               # Dataset documentation and processed data
├── visualizations/     # Charts and analytical outputs
├── dashboard/          # Dashboard application (Week 5)
└── requirements.txt    # Python dependencies

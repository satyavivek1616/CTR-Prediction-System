# CTR Prediction System

An end-to-end Machine Learning project for predicting Advertisement Click Through Rate (CTR) using the Criteo dataset.

---

# Project Overview

This project predicts the probability of a user clicking on an advertisement based on anonymized numerical and categorical features.

The project covers:
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Missing Value Analysis
- Machine Learning Modeling
- Threshold Tuning
- XGBoost Optimization
- SHAP Explainability
- Flask Deployment

---

# Business Problem

Online advertising platforms such as Google Ads, YouTube, Instagram, and Facebook need to decide:

- Which advertisement should be shown?
- Which users are more likely to click?
- How should advertisements be ranked?

CTR prediction helps improve:
- Ad targeting
- Revenue generation
- User engagement
- Recommendation quality

---

# Dataset

Dataset Used:
- Criteo CTR Prediction Dataset

Features:
- 13 Numerical Features
- 26 Categorical Features
- Binary Target Label

Target:
- 1 → Clicked
- 0 → Not Clicked

---

# Exploratory Data Analysis

Performed:
- Null value analysis
- CTR variation analysis
- Feature importance exploration
- Numerical vs categorical analysis
- Missingness signal analysis
- Power BI visualizations

Key Findings:
- Missing values themselves carried predictive signal
- Numerical features contributed strongly to prediction
- Some categorical features showed weak standalone signal
- Feature importance aligned with behavioral patterns

---

# Machine Learning Workflow

```text
EDA
→ Data Cleaning
→ Missing Value Handling
→ Encoding
→ Feature Engineering
→ Logistic Regression Baseline
→ Threshold Tuning
→ XGBoost Modeling
→ SHAP Explainability
→ Flask Deployment
```

---

# Models Used

## Logistic Regression
Used as baseline model for comparison.

## XGBoost
Used for final optimized prediction model.

---

# Model Performance

| Model | ROC-AUC Score |
|------|------|
| Logistic Regression | 0.62 |
| XGBoost | 0.76 |

---

# Key Learnings

- Handling imbalanced datasets
- Importance of ROC-AUC in ranking systems
- Precision vs Recall tradeoff
- Threshold tuning for business objectives
- Feature importance interpretation
- Explainable AI using SHAP
- End-to-end ML deployment using Flask

---

# SHAP Explainability

Used SHAP values to:
- Interpret feature contributions
- Understand prediction behavior
- Analyze positive and negative feature impact

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- Flask
- HTML
- CSS
- Power BI

---

# Flask Deployment

Built a simple web application where users can:
- Input feature values
- Predict click probability
- Interact with trained ML model through browser

---

# Future Improvements

- Better categorical encoding
- Deep Learning CTR models
- Real-time API deployment
- Docker containerization
- Advanced frontend dashboard
- Recommendation system integration

---

# Project Structure

```text
CTR_Prediction_App/
│
├── app.py
├── model.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

# Author

V Satya Vivek
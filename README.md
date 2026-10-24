# 🛡️ FinTech AI Security Guard

[![Streamlit App](https://fintech-fraud-guard.streamlit.app)]

## Overview
This project is a machine learning-based fraud detection API designed for mobile money and FinTech platforms. It evaluates transaction parameters in real-time to identify and block fraudulent activities, specifically optimized for highly imbalanced datasets.

## Architecture: The Hybrid Engine
This system employs a B2B **Hybrid AI-ML Framework** to balance regulatory explainability with advanced behavioral detection:
1. **Rule-Based Gateway:** Intercepts obvious, high-risk anomalies (e.g., massive late-night transfers) for instant, explainable blocking.
2. **Machine Learning Classifier:** A Random Forest model analyzes subtle behavioral patterns (like complete account liquidation or mule account routing) that bypass standard rules.

## Data & Methodology
* **Dataset:** Built using the [PaySim mobile money dataset](https://www.kaggle.com/datasets/ealaxi/paysim1), simulating realistic African FinTech transaction logs.
* **Class Imbalance:** Addressed a severe 99.87% (Safe) to 0.13% (Fraud) imbalance using **SMOTE** (Synthetic Minority Over-sampling Technique).
* **Evaluation Metric:** Optimized for **Recall** to minimize False Negatives and prioritize preventing financial loss over baseline accuracy.

## Tech Stack
* **Frontend/Deployment:** Streamlit, Streamlit Community Cloud
* **Model Training:** Scikit-Learn, Imbalanced-Learn (SMOTE)
* **Data Manipulation:** Pandas, NumPy
* **Serialization:** Joblib

## Local Installation
To run this dashboard locally on your machine:
```bash
# Clone the repository
git clone [https://github.com/henryjnr777-pixel/FinTech-Fraud-Guard.git](https://github.com/henryjnr777-pixel/FinTech-Fraud-Guard.git)

# Navigate into the directory
cd FinTech-Fraud-Guard

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m streamlit run app.py

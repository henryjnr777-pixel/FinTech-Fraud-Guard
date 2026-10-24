import streamlit as st
import pandas as pd
import joblib

# 1. Page Configuration
st.set_page_config(page_title="AI Fraud Guard",
                   page_icon="🛡️", layout="centered")
st.title("🛡️ FinTech AI Security Guard API")
st.write("Enter the transaction details below to simulate the real-time fraud detection gateway.")

# 2. Load the Pre-trained Model


@st.cache_resource
def load_model():
    return joblib.load('fraud_model.pkl')


model_package = load_model()
model = model_package['model']
expected_features = model_package['features']

# 3. Predictor Form (User Interface)
st.subheader("Transaction Parameters")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.markdown("#### 📤 Sender Details")
    amount = st.number_input("Transaction Amount (NGN)",
                             min_value=0.0, value=15000.00, step=1000.0, format="%.2f")
    oldbalanceOrg = st.number_input(
        "Sender's Original Balance", min_value=0.0, value=50000.00, step=1000.0, format="%.2f")
    newbalanceOrig = st.number_input(
        "Sender's New Balance", min_value=0.0, value=35000.00, step=1000.0, format="%.2f")

with col2:
    st.markdown("#### 📥 Receiver Details")
    trans_type = st.selectbox(
        "Transaction Type", ["TRANSFER", "CASH_OUT", "PAYMENT", "DEBIT"])
    oldbalanceDest = st.number_input(
        "Receiver's Original Balance", min_value=0.0, value=10000.00, step=1000.0, format="%.2f")
    newbalanceDest = st.number_input(
        "Receiver's New Balance", min_value=0.0, value=25000.00, step=1000.0, format="%.2f")

st.markdown("#### 🕒 Environmental Context")
step = st.slider("Hour of Transaction (0 = Midnight, 23 = 11 PM)", 0, 23, 14)

st.write("")

# 4. Processing the Inputs on Button Click
if st.button("🛡️ Verify Transaction Live", type="primary", use_container_width=True):
    # Create a dictionary matching the training format, defaulting all dummy types to 0
    input_data = {col: 0 for col in expected_features}

    # Map the user inputs to the correct dictionary keys
    input_data['step'] = step
    input_data['amount'] = amount
    input_data['oldbalanceOrg'] = oldbalanceOrg
    input_data['newbalanceOrig'] = newbalanceOrig
    input_data['oldbalanceDest'] = oldbalanceDest
    input_data['newbalanceDest'] = newbalanceDest

    # Map the selected transaction type to the correct dummy column
    type_column = f"type_{trans_type}"
    if type_column in input_data:
        input_data[type_column] = 1

    # Convert to DataFrame
    df_input = pd.DataFrame([input_data])

    # 5. Hybrid Engine: Rule-Based Check First
    if amount > 1000000 and step >= 1 and step <= 4:
        st.divider()
        st.error("🚨 **TRANSACTION BLOCKED (Rule-Based Engine)**")
        st.write("**Risk Score:** 100.00% (Manual Override)")
        st.write("This transaction triggered a critical security rule (High value during abnormal hours) and was blocked before reaching the AI.")

    else:
        # 6. Fallback to ML Model for complex behavioral checks
        prediction = model.predict(df_input)
        probability = model.predict_proba(df_input)[0][1] * 100

        st.divider()
        if prediction[0] == 1:
            st.error("🚨 **TRANSACTION BLOCKED (AI Model)**")
            st.write(f"**Risk Score:** {probability:.2f}%")
            st.write("This pattern matches known financial theft metrics.")
        else:
            st.success("✅ **TRANSACTION APPROVED (AI Model)**")
            st.write(f"**Risk Score:** {probability:.2f}%")
            st.write(
                "This transaction aligns with standard customer behavioral metrics.")

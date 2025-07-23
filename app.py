import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Fraud Detection App", layout="wide")
st.title("🛡️ Credit Card Fraud Detection Web App")

model = joblib.load("fraud_detection_model.pkl")

st.markdown("Upload a CSV file or enter transaction details manually.")

uploaded_file = st.file_uploader("📂 Upload CSV File with V1–V28 and Amount", type="csv")

if uploaded_file:
    try:
        data = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(data.head())

        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data)
        predictions = model.predict(scaled_data)
        data['Prediction'] = predictions

        st.write("Prediction Results:")
        st.dataframe(data[['Prediction']])
        st.success(f"⚠️ Fraudulent Transactions Detected: {sum(predictions)}")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.subheader("✍️ Manual Transaction Entry")

with st.form("manual_form"):
    inputs = {}
    cols = st.columns(5)
    for i in range(1, 29):
        col = cols[(i - 1) % 5]
        inputs[f'V{i}'] = col.number_input(f'V{i}', value=0.0)

    amount = st.number_input("Amount", value=100.0)
    submit = st.form_submit_button("Predict Fraud")

    if submit:
        row = [inputs[f'V{i}'] for i in range(1, 29)] + [amount]
        input_df = pd.DataFrame([row], columns=[f'V{i}' for i in range(1, 29)] + ['Amount'])
        scaled_input = StandardScaler().fit_transform(input_df)
        prediction = model.predict(scaled_input)[0]
        if prediction == 1:
            st.error("❌ Fraudulent Transaction Detected!")
        else:
            st.success("✅ Transaction Looks Legitimate.")

# frontend/app.py

import streamlit as st
import requests

st.set_page_config(page_title="Loan Approval Predictor", layout="centered")

st.title("🏦 Smart Loan Approval Prediction")
st.markdown("Fill out the loan application form below:")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=1)
loan_term = st.selectbox("Loan Term (in days)", [360, 180, 240, 120, 300])
credit_history = st.selectbox("Credit History (1: good, 0: bad)", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# Submit
if st.button("Predict Loan Approval"):
    with st.spinner("Predicting..."):
        data = {
            "Gender": gender,
            "Married": married,
            "Dependents": dependents,
            "Education": education,
            "Self_Employed": self_employed,
            "ApplicantIncome": applicant_income,
            "CoapplicantIncome": coapplicant_income,
            "LoanAmount": loan_amount,
            "Loan_Amount_Term": loan_term,
            "Credit_History": credit_history,
            "Property_Area": property_area
        }

        try:
            res = requests.post("http://127.0.0.1:8000/predict", json=data)
            result = res.json()["result"]
            st.success(f"Prediction: {result}")
        except Exception as e:
            st.error(f"❌ Failed to get prediction. Error: {str(e)}")

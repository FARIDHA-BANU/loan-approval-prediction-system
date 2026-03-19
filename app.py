import streamlit as st
import numpy as np
import joblib

model = joblib.load("model/loan_model.pkl")

st.title("AI Loan Approval Predictor")

income = st.number_input("Income")
loan = st.number_input("Loan Amount")
term = st.number_input("Loan Term")
cibil = st.number_input("CIBIL Score")

if st.button("Predict"):
    data = np.array([[income, loan, term, cibil]])
    prediction = model.predict(data)[0]
    
    if prediction == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")
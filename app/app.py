import streamlit as st
import joblib
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Load the model.
try:
    model = joblib.load('models/loan_eligibility_model7.pkl')  # Ensure the correct path to the model
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading the model: {e}")

# App title
st.title('Loan Eligibility Model')

# User inputs
income = st.number_input('Monthly income', min_value=0)  # Monthly income
credit_score = st.number_input('Credit score', min_value=0)  # Credit score

logging.info(f"User input - Monthly income: {income}, Credit score: {credit_score}")

# Check thresholds for credit score and income before prediction
def check_eligibility(income, credit_score):
    if credit_score < 750:
        return 0, "Loan denied due to low credit score"
    if income < 3000:
        return 0, "Loan denied due to low income"
    return 1, "Loan approved based on both income and credit score"

if st.button('Predict'):
    result, reason = check_eligibility(income, credit_score)  # Eligibility check first
    if result == 0:
        st.write(f"Reason: {reason}")  # Display reason for loan rejection
        logging.info(f"The loan has not been approved. Reason: {reason}")
    else:
        st.write(f"Reason: {reason}")  # Display reason for loan approval
        logging.info(f"The loan has been approved. Reason: {reason}")

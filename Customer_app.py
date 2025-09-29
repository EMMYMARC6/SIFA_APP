

import streamlit as st
import pandas as pd
import pickle

# Load the saved model
loaded_model = pickle.load(open("customer_churn.sav", "rb"))

# Streamlit App
st.title("Customer Churn Prediction System")
st.markdown("Predict if a customer is likely to churn based on their account details.")

# Sidebar inputs
st.sidebar.header("Customer Details")

tenure = st.sidebar.number_input("Tenure (months)", min_value=0, max_value=100, value=5)
monthly_charges = st.sidebar.number_input("Monthly Charges", min_value=0.0, value=70.35)
total_charges = st.sidebar.number_input("Total Charges", min_value=0.0, value=350.5)

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
phone_service = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.sidebar.selectbox("Multiple Lines", ["Yes", "No"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.sidebar.selectbox("Online Security", ["Yes", "No"])
online_backup = st.sidebar.selectbox("Online Backup", ["Yes", "No"])
device_protection = st.sidebar.selectbox("Device Protection", ["Yes", "No"])
tech_support = st.sidebar.selectbox("Tech Support", ["Yes", "No"])
streaming_tv = st.sidebar.selectbox("Streaming TV", ["Yes", "No"])
streaming_movies = st.sidebar.selectbox("Streaming Movies", ["Yes", "No"])
contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.sidebar.selectbox("Payment Method", ["Electronic check", "Mailed check",
                                                         "Bank transfer (automatic)", "Credit card (automatic)"])

# Mapping categorical values
mapping = {
    'Yes': 1, 'No': 0, 'Male': 1, 'Female': 0,
    'DSL': 1, 'Fiber optic': 2, 'No': 0,
    'Month-to-month': 0, 'One year': 1, 'Two year': 2,
    'Electronic check': 0, 'Mailed check': 1,
    'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3
}

# Prepare input dataframe
# Prepare input dataframe
input_data = pd.DataFrame({
    'tenure': [tenure],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges],
    'gender': [gender],
    'SeniorCitizen': [senior_citizen],
    'Partner': [partner],
    'Dependents': [dependents],
    'PhoneService': [phone_service],
    'MultipleLines': [multiple_lines],
    'InternetService': [internet_service],
    'OnlineSecurity': [online_security],
    'OnlineBackup': [online_backup],
    'DeviceProtection': [device_protection],
    'TechSupport': [tech_support],
    'StreamingTV': [streaming_tv],
    'StreamingMovies': [streaming_movies],
    'Contract': [contract],
    'PaperlessBilling': [paperless_billing],
    'PaymentMethod': [payment_method]
})

# Predict button
if st.button("Predict Churn"):
    predicted_churn = loaded_model.predict(input_data)[0]
    if predicted_churn == 0:
        st.success("The customer is NOT likely to churn ")
    else:
        st.error("The customer IS likely to churn ")

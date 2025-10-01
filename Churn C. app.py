import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# 1) Load model and encoders
# -----------------------------
model = pickle.load(open("churn_model.pkl", "rb"))

# Load encoders dictionary (if you saved them)
try:
    encoders = pickle.load(open("label_encoders.pkl", "rb"))
except:
    encoders = {}

# -----------------------------
# 2) Streamlit App UI
# -----------------------------
st.title("📊 Customer Churn Prediction App")
st.write("Predict whether a telecom customer is likely to churn or not. please enter credentials")

# Example input fields (adjust according to your dataset)
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=1)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=100.0)

# -----------------------------
# 3) Preprocess input
# -----------------------------
input_dict = {
    "gender": gender,
    "SeniorCitizen": senior,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": multiple_lines,
    "OnlineSecurity": online_security,
    "OnlineBackup": online_backup,
    "DeviceProtection": device_protection,
    "TechSupport": tech_support,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "Contract": contract,
    "PaperlessBilling": paperless,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
}

Churn_dataset = pd.DataFrame([input_dict])

# Apply label encoders if available
for col, le in encoders.items():
    if col in Churn_dataset.columns:
        try:
            Churn_dataset[col] = le.transform(Churn_dataset[col])
        except:
            st.warning(f"⚠️ Unknown label in column {col}, defaulting to 0")
            Churn_dataset[col] = 0

# -----------------------------
# 4) Prediction
# -----------------------------
if st.button("Predict Churn"):
    prediction = model.predict(Churn_dataset)[0]
    if prediction == 1:
        st.error("❌ The customer is **likely to churn**. Take retention actions!")
    else:
        st.success("✅ The customer is **not likely to churn**.")

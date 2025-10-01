# app.py

import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load trained pipeline
# -------------------------------
@st.cache_data
def load_model():
    return pickle.load(open("customer_churn.sav", "rb"))

loaded_model = load_model()

# -------------------------------
# Get numeric and categorical columns
# -------------------------------
numeric_features = loaded_model.named_steps['preprocessor'].transformers_[0][2]
categorical_features = loaded_model.named_steps['preprocessor'].transformers_[1][2]
expected_cols = list(numeric_features) + list(categorical_features)

# -------------------------------
# Streamlit App
# -------------------------------
st.title("Customer Churn Prediction")

st.write("Enter customer information to predict if they are likely to churn:")

# -------------------------------
# User input
# -------------------------------
def get_user_input():
    data = {}
    
    # Numeric inputs
    for feature in numeric_features:
        data[feature] = [st.number_input(feature, min_value=0.0, value=0.0)]
    
    # Categorical inputs
    for feature in categorical_features:
        data[feature] = [st.selectbox(feature, ["Yes", "No", "Male", "Female",
                                               "Month-to-month", "One year", "Two year",
                                               "Electronic check", "Mailed check", 
                                               "Bank transfer (automatic)", "Credit card (automatic)",
                                               "DSL", "Fiber optic", "No"])]

    return pd.DataFrame(data)

input_data = get_user_input()

# -------------------------------
# Handle missing columns
# -------------------------------
for col in expected_cols:
    if col not in input_data.columns:
        if col in numeric_features:
            input_data[col] = 0
        else:
            input_data[col] = 'No'

# Reorder columns
input_data = input_data[expected_cols]

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Churn"):
    prediction = loaded_model.predict(input_data)[0]
    
    if prediction == 0:
        st.success("✅ The customer is NOT likely to churn")
    else:
        st.error("⚠️ The customer IS likely to churn")

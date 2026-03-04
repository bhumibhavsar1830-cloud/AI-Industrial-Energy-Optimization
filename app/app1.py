import os
import pickle
import streamlit as st
import numpy as np

# Page configuration
st.set_page_config(page_title="AI Industrial Carbon Predictor", layout="wide")

st.title("🌍 AI Industrial Carbon Emission Predictor")

# Updated model path
model_path = "carbon_model.pkl"

# Load model safely
if not os.path.exists(model_path):
    st.error("Model file not found! Please ensure carbon_model.pkl is in the app folder.")
    st.stop()

with open(model_path, "rb") as f:
    model_data = pickle.load(f)  # model_data is a dict

model = model_data["model"]
feature_order = model_data["features"]

st.success("Model Loaded Successfully ✅")

# Sidebar inputs
st.sidebar.header("Enter Industrial Parameters")
units = st.sidebar.number_input("Units Produced", min_value=0, value=500)
energy = st.sidebar.number_input("Energy Consumption (kWh)", min_value=0.0, value=1000.0)
renewable = st.sidebar.slider("Renewable Energy Percentage", 0, 100, 20)
downtime = st.sidebar.number_input("Machine Downtime (Hours)", min_value=0.0, value=5.0)
efficiency = st.sidebar.number_input("Energy Efficiency Index", min_value=0.0, value=75.0)

if st.button("Predict Carbon Emissions"):
    input_dict = {
        'Units_Produced': units,
        'Energy_Consumption_kWh': energy,
        'Renewable_Energy_Percentage': renewable,
        'Machine_Downtime_Hours': downtime,
        'Energy_Efficiency_Index': efficiency
    }

    input_data = np.array([[input_dict[col] for col in feature_order]])
    prediction = model.predict(input_data)[0]

    st.success(f"🌱 Predicted Carbon Emissions: {prediction:.2f} tons")

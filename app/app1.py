import os
import pickle
import streamlit as st
import numpy as np

# Page configuration
st.set_page_config(page_title="AI Industrial Energy Optimizer", layout="wide")

st.title("⚡ AI Industrial Energy & Carbon Predictor")

# Correct path to model
model_path = "../ml_model/carbon_model.pkl"

# Load model safely
if os.path.exists(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
else:
    st.error("❌ Model file not found!")
    st.stop()

st.sidebar.header("Input Parameters")

# IMPORTANT: These must match training features EXACTLY

units = st.sidebar.number_input("Units Produced", min_value=0, value=500)
energy = st.sidebar.number_input("Energy Consumption (kWh)", min_value=0.0, value=1000.0)
renewable = st.sidebar.slider("Renewable Energy Percentage", 0, 100, 20)
downtime = st.sidebar.number_input("Machine Downtime (Hours)", min_value=0.0, value=5.0)
efficiency = st.sidebar.number_input("Energy Efficiency Index", min_value=0.0, value=75.0)

if st.button("Predict Carbon Emissions"):

    # Must follow SAME ORDER as training
    input_data = np.array([[units,
                            energy,
                            renewable,
                            downtime,
                            efficiency]])

    prediction = model.predict(input_data)[0]

    st.success(f"🌍 Predicted Carbon Emissions: {prediction:.2f} tons")

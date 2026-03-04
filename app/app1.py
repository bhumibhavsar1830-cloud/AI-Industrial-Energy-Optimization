import os
import pickle
import streamlit as st
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="AI Energy Optimizer", layout="wide")

# Correct paths
model_path = "../ml_model/carbon_model.pkl"
data_path = "../data/energy_data.csv"

# Load dataset
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
else:
    st.error(f"Data file not found: {data_path}")
    st.stop()

# Load model
if os.path.exists(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    st.success("Model loaded successfully!")
else:
    st.error(f"Model file not found: {model_path}")
    st.stop()

# Sidebar Inputs
units = st.sidebar.number_input("Units Produced", 400, 1000, 600)
renewable = st.sidebar.slider("Renewable Energy %", 0, 100, 20)
downtime = st.sidebar.number_input("Machine Downtime (Hours)", 0, 50, 5)
temperature = st.sidebar.number_input("Avg Temperature (°C)", 10, 50, 28)

if st.button("Predict Energy Consumption"):
    input_data = np.array([[units, renewable, downtime, temperature]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Energy Consumption: {prediction:.2f} kWh")

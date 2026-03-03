import streamlit as st
import pandas as pd
import pickle
import numpy as np

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="AI Energy Optimizer", layout="wide")

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("energy_data.csv")

# -----------------------------
# Load model
# -----------------------------
model = pickle.load(open("carbon_model.pkl", "rb"))

# -----------------------------
# Title Section
# -----------------------------
st.title("⚡ AI-Based Industrial Energy Optimization System")
st.subheader("Predict • Optimize • Reduce Cost & Emissions")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Input Parameters")

units = st.sidebar.number_input("Units Produced", 400, 1000, 600)
renewable = st.sidebar.slider("Renewable Energy %", 0, 100, 20)
downtime = st.sidebar.number_input("Machine Downtime (Hours)", 0, 50, 5)
temperature = st.sidebar.number_input("Average Temperature (°C)", 10, 50, 28)

# -----------------------------
# Prediction Section
# -----------------------------
if st.button("Predict Energy Consumption"):

    input_data = np.array([[units, renewable, downtime, temperature]])
    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Energy Consumption: {prediction:.2f} kWh")

    if renewable < 20:
        st.warning("⚠ Increase renewable energy usage to reduce carbon emissions.")

    if downtime > 10:
        st.warning("⚠ Reduce machine downtime to improve efficiency.")

    if temperature > 32:
        st.info("ℹ High temperature increases energy consumption. Consider cooling optimization.")

    cost_saving = prediction * 0.05
    st.success(f"Estimated Monthly Cost Saving: ${cost_saving:.2f}")

# -----------------------------
# Visualization
# -----------------------------
st.subheader("📊 Energy Consumption Trend")
st.line_chart(df["Energy_Consumption_kWh"])

st.subheader("🌱 Carbon Emissions vs Renewable Usage")
st.bar_chart(df[["Carbon_Emissions_tons", "Renewable_Energy_Percentage"]])

st.markdown("---")
st.markdown("Built for Sustainable Industry Hackathon 2026 🚀")


import streamlit as st
import pandas as pd
import pickle

# Load dataset
df = pd.read_csv("energy_data.csv")

# Load model
model = pickle.load(open("carbon_model.pkl", "rb"))

st.title("⚡ AI-Based Industrial Energy Optimization System")
st.subheader("Predict • Optimize • Reduce Cost & Emissions")

# Sidebar Inputs
units = st.sidebar.number_input("Units Produced", 400, 1000)
renewable = st.sidebar.slider("Renewable Energy %", 0, 100)
downtime = st.sidebar.number_input("Machine Downtime (Hours)", 0, 50)
temperature = st.sidebar.number_input("Average Temperature (°C)", 10, 50)

if st.button("Predict Energy Consumption"):

    prediction = model.predict([[units, renewable, downtime, temperature]])

    st.success(f"Predicted Energy Consumption: {prediction[0]:.2f} kWh")

    if renewable < 20:
        st.warning("Increase renewable energy usage to reduce carbon emissions.")

    if downtime > 10:
        st.warning("Reduce machine downtime to improve efficiency.")

    if temperature > 32:
        st.info("High temperature increases energy consumption. Consider cooling optimization.")

    cost_saving = prediction[0] * 0.05
    st.success(f"Estimated Monthly Cost Saving: ${cost_saving:.2f}")

st.line_chart(df["Energy_Consumption_kWh"])
st.bar_chart(df[["Carbon_Emissions_tons", "Renewable_Energy_Percentage"]])

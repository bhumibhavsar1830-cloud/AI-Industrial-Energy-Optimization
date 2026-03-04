import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("data/energy_data.csv")

# Define features (ORDER MATTERS)
feature_columns = [
    'Units_Produced',
    'Energy_Consumption_kWh',
    'Renewable_Energy_Percentage',
    'Machine_Downtime_Hours',
    'Energy_Efficiency_Index'
]

X = data[feature_columns]
y = data['Carbon_Emissions_tons']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Print accuracy
print("Model R2 Score:", model.score(X_test, y_test))

# Save BOTH model and feature order (important)
model_data = {
    "model": model,
    "features": feature_columns
}

with open("ml_model/carbon_model.pkl", "wb") as f:
    pickle.dump(model_data, f)

print("Model saved successfully inside ml_model/")

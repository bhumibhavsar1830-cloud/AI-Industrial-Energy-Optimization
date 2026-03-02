import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv('../data/energy_data.csv')

# Features (input variables)
X = data[['Units_Produced',
          'Energy_Consumption_kWh',
          'Renewable_Energy_Percentage',
          'Machine_Downtime_Hours',
          'Energy_Efficiency_Index']]

# Target (what we predict)
y = data['Carbon_Emissions_tons']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open('carbon_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved successfully!")

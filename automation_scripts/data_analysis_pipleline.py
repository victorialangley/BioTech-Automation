"""
data_analysis_pipeline.py
Author: Victoria Langley
Description: This script demonstrates a simplified data analysis pipeline for biotech experiments.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load experimental data
data = pd.read_csv("experiment_data.csv")

# Data preprocessing
X = data.drop(columns=["target"])
y = data["target"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

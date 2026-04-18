import pandas as pd
import numpy as np

np.random.seed(42)

# Create date range (20 years monthly)
dates = pd.date_range(start="2000-01-01", periods=240, freq="ME")

# Trend (warming)
trend = 0.02 * np.arange(240)

# Seasonal pattern
seasonality = 2 * np.sin(2 * np.pi * np.arange(240) / 12)

# Temperature
temperature = 15 + trend + seasonality + np.random.normal(0, 0.5, 240)

# Rainfall
rainfall = 100 + 20 * np.sin(2 * np.pi * np.arange(240) / 12) + np.random.normal(0, 10, 240)

# CO2 trend
co2 = 370 + 0.8 * np.arange(240) + np.random.normal(0, 1, 240)

# Sea level
sea_level = 0.3 * np.arange(240) + np.random.normal(0, 0.2, 240)

# Add anomalies
anomaly_indices = np.random.choice(range(240), size=10, replace=False)
temperature[anomaly_indices] += np.random.choice([3, -3], size=10)

# Create dataframe
df = pd.DataFrame({
    "Date": dates,
    "Temperature": temperature,
    "Rainfall": rainfall,
    "CO2": co2,
    "Sea_Level": sea_level
})

# Save file
df.to_csv("data/raw/climate_data.csv", index=False)

print("Dataset generated successfully ✅")
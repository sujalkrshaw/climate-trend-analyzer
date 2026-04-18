import pandas as pd

from src.feature_engineering import feature_engineering
from src.eda import (
    plot_temperature_trend,
    plot_rainfall_trend,
    plot_season_distribution,
    plot_correlation,
    plot_trend_with_regression,
    plot_anomalies,
    plot_forecast
)
from src.analysis import (
    trend_analysis,
    detect_anomalies,
    forecast_temperature
)


# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("data/raw/climate_data.csv")


# -------------------------------
# FEATURE ENGINEERING
# -------------------------------
df = feature_engineering(df)


# -------------------------------
# EDA
# -------------------------------
plot_temperature_trend(df)
plot_rainfall_trend(df)
plot_season_distribution(df)
plot_correlation(df)


# -------------------------------
# ANALYSIS
# -------------------------------
df = trend_analysis(df)
df = detect_anomalies(df)


# -------------------------------
# FORECAST
# -------------------------------
forecast = forecast_temperature(df)


# -------------------------------
# ADVANCED VISUALS
# -------------------------------
plot_trend_with_regression(df)
plot_anomalies(df)
plot_forecast(df, forecast)


print("\n✅ PROJECT EXECUTED SUCCESSFULLY")
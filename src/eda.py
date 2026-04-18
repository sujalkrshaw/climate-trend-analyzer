import os
os.makedirs("outputs/plots", exist_ok=True)

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# -------------------------------
# BASIC EDA PLOTS
# -------------------------------

def plot_temperature_trend(df):
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Temperature'], label='Temperature', alpha=0.5)
    plt.plot(df['Date'], df['Temp_Rolling_Mean'], color='red', label='Trend')
    plt.title('Temperature Trend Over Time')
    plt.legend()
    plt.grid()
    plt.savefig('outputs/plots/temperature_trend.png')
    plt.close()


def plot_rainfall_trend(df):
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Rainfall'], label='Rainfall', alpha=0.5)
    plt.plot(df['Date'], df['Rain_Rolling_Mean'], color='blue', label='Trend')
    plt.title('Rainfall Trend Over Time')
    plt.legend()
    plt.grid()
    plt.savefig('outputs/plots/rainfall_trend.png')
    plt.close()


def plot_season_distribution(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x='Season', data=df)
    plt.title('Season Distribution')
    plt.savefig('outputs/plots/season_distribution.png')
    plt.close()


def plot_correlation(df):
    plt.figure(figsize=(6,5))
    sns.scatterplot(x='CO2', y='Temperature', data=df)
    plt.title('CO2 vs Temperature')
    plt.savefig('outputs/plots/co2_vs_temp.png')
    plt.close()


# -------------------------------
# ADVANCED VISUALS
# -------------------------------

def plot_trend_with_regression(df):
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Temperature'], label='Temperature', alpha=0.5)
    plt.plot(df['Date'], df['Trend_Line'], color='green', label='Trend Line')
    plt.title('Temperature Trend with Regression')
    plt.legend()
    plt.grid()
    plt.savefig('outputs/plots/trend_regression.png')
    plt.close()


def plot_anomalies(df):
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Temperature'], label='Temperature')

    anomalies = df[df['Anomaly'] == 1]
    plt.scatter(anomalies['Date'], anomalies['Temperature'],
                color='red', label='Anomalies')

    plt.title('Anomaly Detection')
    plt.legend()
    plt.grid()
    plt.savefig('outputs/plots/anomalies.png')
    plt.close()


def plot_forecast(df, forecast):
    future_dates = pd.date_range(start=df['Date'].iloc[-1], periods=12, freq='ME')

    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Temperature'], label='Historical')
    plt.plot(future_dates, forecast, color='orange', label='Forecast')

    plt.title('Temperature Forecast')
    plt.legend()
    plt.grid()
    plt.savefig('outputs/plots/forecast.png')
    plt.close()
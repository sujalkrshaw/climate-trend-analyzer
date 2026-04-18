import numpy as np
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA


def trend_analysis(df):
    df = df.copy()
    df['Time_Index'] = np.arange(len(df))

    X = df[['Time_Index']]
    y = df['Temperature']

    model = LinearRegression()
    model.fit(X, y)

    df['Trend_Line'] = model.predict(X)

    print(f"Trend slope (warming rate): {model.coef_[0]:.4f} °C per month")

    return df


def detect_anomalies(df):
    df = df.copy()

    mean = df['Temperature'].mean()
    std = df['Temperature'].std()

    df['Z_Score'] = (df['Temperature'] - mean) / std
    df['Anomaly'] = np.where(abs(df['Z_Score']) > 2, 1, 0)

    print(f"Total anomalies detected: {df['Anomaly'].sum()}")

    return df


def forecast_temperature(df):
    model = ARIMA(df['Temperature'], order=(1,1,1))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=12)

    print("\nNext 12 months forecast:")
    print(forecast)

    return forecast

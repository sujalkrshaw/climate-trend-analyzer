import pandas as pd


def feature_engineering(df):
    df['Date'] = pd.to_datetime(df['Date'])

    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month

    def get_season(month):
        if month in [12,1,2]:
            return "Winter"
        elif month in [3,4,5]:
            return "Summer"
        elif month in [6,7,8]:
            return "Monsoon"
        else:
            return "Post-Monsoon"

    df['Season'] = df['Month'].apply(get_season)

    df['Temp_Lag1'] = df['Temperature'].shift(1)
    df['Rain_Lag1'] = df['Rainfall'].shift(1)

    df['Temp_Rolling_Mean'] = df['Temperature'].rolling(12).mean()
    df['Rain_Rolling_Mean'] = df['Rainfall'].rolling(12).mean()

    df = df.dropna()

    return df
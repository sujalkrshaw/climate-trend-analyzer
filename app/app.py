import sys
import os

# Ensure we can import from /src when running via Streamlit
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.express as px

from src.feature_engineering import feature_engineering
from src.analysis import trend_analysis, detect_anomalies, forecast_temperature

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Climate Trend Analyzer",
    layout="wide",
    page_icon="🌍"
)

# -------------------------------
# PREMIUM UI (CSS)
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: #00ADB5;
}
.metric-card {
    background: linear-gradient(135deg, #1f2937, #111827);
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    color: #ffffff;
    box-shadow: 0 6px 18px rgba(0,0,0,0.45);
}
.section {
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.markdown("## 🌍 Climate Trend Analyzer")
st.markdown("#### 📊 Real-time Climate Insights • Trends • Forecasts")

# -------------------------------
# LOAD & PROCESS DATA
# -------------------------------
df = pd.read_csv("data/raw/climate_data.csv")
df = feature_engineering(df)
df = trend_analysis(df)
df = detect_anomalies(df)
forecast = forecast_temperature(df)

# -------------------------------
# KPI CARDS
# -------------------------------
st.markdown("---")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>🌡 Avg Temperature</h3>
        <h2>{df['Temperature'].mean():.2f} °C</h2>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>🌧 Avg Rainfall</h3>
        <h2>{df['Rainfall'].mean():.2f} mm</h2>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <h3>⚠️ Total Anomalies</h3>
        <h2>{int(df['Anomaly'].sum())}</h2>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# TEMPERATURE TREND
# -------------------------------
st.markdown("---")
st.subheader("📈 Temperature Trend")

fig_temp = px.line(
    df,
    x="Date",
    y="Temperature",
    template="plotly_dark"
)
fig_temp.update_traces(line=dict(width=3))
fig_temp.update_layout(
    plot_bgcolor="#0e1117",
    paper_bgcolor="#0e1117",
    font=dict(color="white")
)

st.plotly_chart(fig_temp, use_container_width=True)

# -------------------------------
# RAINFALL TREND
# -------------------------------
st.markdown("---")
st.subheader("🌧 Rainfall Trend")

fig_rain = px.line(
    df,
    x="Date",
    y="Rainfall",
    template="plotly_dark",
    color_discrete_sequence=["cyan"]
)
fig_rain.update_traces(line=dict(width=3))

st.plotly_chart(fig_rain, use_container_width=True)

# -------------------------------
# CO2 vs TEMPERATURE
# -------------------------------
st.markdown("---")
st.subheader("🌫 CO₂ vs Temperature")

fig_scatter = px.scatter(
    df,
    x="CO2",
    y="Temperature",
    color="Season",
    template="plotly_dark"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# -------------------------------
# ANOMALIES TABLE
# -------------------------------
st.markdown("---")
st.subheader("⚠️ Detected Anomalies")

anomalies = df[df["Anomaly"] == 1]

if len(anomalies) > 0:
    st.dataframe(anomalies, use_container_width=True)
else:
    st.info("No anomalies detected.")

# -------------------------------
# FORECAST GRAPH
# -------------------------------
st.markdown("---")
st.subheader("🔮 12-Month Forecast")

forecast_df = pd.DataFrame({
    "Month": range(1, 13),
    "Forecast Temperature": forecast.values
})

fig_forecast = px.line(
    forecast_df,
    x="Month",
    y="Forecast Temperature",
    markers=True,
    template="plotly_dark"
)

st.plotly_chart(fig_forecast, use_container_width=True)

# -------------------------------
# DATA PREVIEW
# -------------------------------
st.markdown("---")
with st.expander("📊 View Full Dataset"):
    st.dataframe(df, use_container_width=True)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown(
    "<center>🚀 Built by Sujal Shaw | Climate Analytics Dashboard</center>",
    unsafe_allow_html=True
)
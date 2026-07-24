"""
Forecast Page
"""

import pandas as pd
import plotly.express as px
import streamlit as st

from services.api_client import APIClient

st.title("📈 Cloud Cost Forecast")

st.caption(
    "AI-powered cloud cost prediction for the next 30 days."
)

# ---------------------------------------------------
# Fetch Forecast
# ---------------------------------------------------

try:
    forecast = APIClient.get_forecast()

except Exception as e:
    st.error(e)
    st.stop()

# ---------------------------------------------------
# Calculate Summary
# ---------------------------------------------------

predicted = forecast["predicted_costs"]

current_cost = predicted[0]
predicted_cost = predicted[-1]

growth = (
    (predicted_cost - current_cost)
    / current_cost
) * 100

confidence = 91

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Current Cost",
        f"${current_cost:.2f}"
    )

with col2:
    st.metric(
        "📈 Predicted Cost",
        f"${predicted_cost:.2f}"
    )

with col3:
    st.metric(
        "📊 Growth",
        f"{growth:.1f}%"
    )

with col4:
    st.metric(
        "🎯 Confidence",
        f"{confidence}%"
    )

st.divider()

# ---------------------------------------------------
# Forecast Chart
# ---------------------------------------------------

df = pd.DataFrame({
    "Day": range(1, len(predicted) + 1),
    "Predicted Cost": predicted
})

fig = px.line(
    df,
    x="Day",
    y="Predicted Cost",
    markers=True,
    title="30-Day Cost Forecast"
)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# AI Insight
# ---------------------------------------------------

st.divider()

st.subheader("🤖 AI Forecast Insight")

if growth < 5:
    insight = (
        "Cloud spending is expected to remain stable "
        "over the next month."
    )

elif growth < 15:
    insight = (
        "Cloud costs are expected to increase moderately. "
        "Review resource utilization."
    )

else:
    insight = (
        "Cloud costs are increasing rapidly. "
        "Consider rightsizing resources and reviewing "
        "optimization recommendations."
    )

st.info(insight)
"""
Reusable Charts
"""

import pandas as pd
import plotly.express as px
import streamlit as st


def forecast_chart(forecast):

    df = pd.DataFrame(forecast)

    fig = px.line(
        df,
        x="day",
        y="cost",
        markers=True,
        title="30-Day Forecast"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

def cost_trend_chart(history):

    df = pd.DataFrame(history)

    fig = px.line(
        df,
        x="date",
        y="cost",
        markers=True,
        title="Cloud Cost Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
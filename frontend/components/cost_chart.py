import pandas as pd
import plotly.express as px
import streamlit as st


def display_cost_chart(metrics):

    df = pd.DataFrame(metrics["cost_history"])

    fig = px.line(
        df,
        x="date",
        y="cost",
        markers=True,
        title="Cloud Cost Trend (Last 7 Days)"
    )

    fig.update_layout(height=400)

    st.plotly_chart(fig, use_container_width=True)
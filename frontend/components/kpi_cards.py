import streamlit as st


def display_kpis(metrics: dict):
    """
    Display dashboard KPI cards.
    """

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💰 Cloud Cost",
            f"${metrics['total_cost']:,.2f}"
        )

    with col2:
        st.metric(
            "💵 Savings",
            f"${metrics['monthly_savings']:,.2f}"
        )

    with col3:
        st.metric(
            "🖥 CPU",
            f"{metrics['cpu_utilization']}%"
        )

    with col4:
        st.metric(
            "🧠 Memory",
            f"{metrics['memory_utilization']}%"
        )
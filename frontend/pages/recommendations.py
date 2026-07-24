"""
Recommendations Page
"""

import streamlit as st

from services.api_client import APIClient


st.title("💡 Cloud Optimization Recommendations")

st.caption(
    "AI-powered recommendations to reduce cloud cost and improve efficiency."
)

# ---------------------------------------------------
# Fetch Recommendations
# ---------------------------------------------------

try:
    response = APIClient.get_recommendations()

except Exception as e:
    st.error(f"Unable to load recommendations.\n\n{e}")
    st.stop()


recommendations = response["recommendations"]

# ---------------------------------------------------
# Summary Cards
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Recommendations",
        response["total_recommendations"]
    )

with col2:
    st.metric(
        "Potential Monthly Savings",
        f"${response['estimated_monthly_savings']:.2f}"
    )

st.divider()

# ---------------------------------------------------
# Category Filter
# ---------------------------------------------------

categories = ["All"]

for rec in recommendations:
    if rec["category"] not in categories:
        categories.append(rec["category"])

selected_category = st.selectbox(
    "Filter by Category",
    categories
)

# ---------------------------------------------------
# Severity Colors
# ---------------------------------------------------

severity_icons = {
    "High": "🔴",
    "Medium": "🟡",
    "Low": "🟢"
}

# ---------------------------------------------------
# Recommendation Cards
# ---------------------------------------------------

filtered = recommendations

if selected_category != "All":
    filtered = [
        rec
        for rec in recommendations
        if rec["category"] == selected_category
    ]

for rec in filtered:

    icon = severity_icons.get(
        rec["severity"],
        "⚪"
    )

    with st.container(border=True):

        col1, col2 = st.columns([4, 1])

        with col1:

            st.markdown(
                f"### {icon} {rec['title']}"
            )

            st.write(rec["description"])

            st.markdown(
                f"**Category:** {rec['category']}"
            )

            st.markdown(
                f"**Severity:** {rec['severity']}"
            )

        with col2:

            st.metric(
                "Savings",
                f"${rec['estimated_savings']:.2f}"
            )

st.divider()

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.success(
    "Review all recommendations before applying them to your production environment."
)
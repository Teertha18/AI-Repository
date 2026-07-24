import streamlit as st

from services.api_client import APIClient

st.set_page_config(
    page_title="AI Insights",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Cloud Architect")

st.caption(
    "AI-powered analysis, prediction and optimization recommendations."
)
st.divider()

st.subheader("🤖 AI Engine")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("LLM Model", "Gemini 2.5")

with c2:
    st.metric("Input", "Historical Metrics")

with c3:
    st.metric("Output", "Predictions")

st.info(
    """
The AI analyzes historical Google Cloud metrics collected from:

• BigQuery
• Dataproc
• Dataflow
• Cloud Storage

It predicts future capacity requirements, explains its reasoning,
recommends optimizations, and estimates business impact.
"""
)

st.divider()

# -----------------------------------------------------

try:
    with st.spinner("🧠 AI is analyzing your cloud environment..."):
        if "analysis" not in st.session_state:
            with st.spinner("🧠 AI is analyzing..."):
                st.session_state.analysis = APIClient.get_analysis()
        analysis = st.session_state.analysis
except Exception as e:
    st.error(e)
    st.stop()

# -----------------------------------------------------

with st.container(border=True):

    st.subheader("🧠 Executive Summary")

    st.write(
        analysis["executive_summary"]
    )

st.divider()

# st.divider()


def health_color(health: str):

    health = health.strip().lower()

    if any(word in health for word in ["critical", "saturated"]):
        return "🔴"

    if any(word in health for word in ["warning", "high"]):
        return "🟡"

    return "🟢"


# -----------------------------------------------------

for service in analysis["services"]:

    icon = health_color(service["health"])

    with st.container(border=True):

        st.subheader(
            f"{icon} {service['service'].title()}"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Current Health",
                service["health"]
            )

            st.metric(
            "Confidence",
            f"{service['confidence']}%"
        )

        st.progress(
            service["confidence"] / 100
        )
        with col2:

            st.success("### 📈 AI Prediction")

            st.write(service["prediction"])

        st.divider()

        with st.expander("🧠 AI Reasoning", expanded=False):
            st.write(service["reasoning"])

        with st.expander("💡 Recommendation", expanded=True):
            st.success(service["recommendation"])

        with st.expander("💼 Business Impact", expanded=False):
            st.warning(service["business_impact"])

    st.write("")


#-----footer-----------------

st.divider()

st.caption(
    "🚀 Cloud Resource Optimization Copilot | FastAPI | Streamlit | Gemini AI | Google Cloud"
)
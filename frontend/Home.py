import streamlit as st

st.set_page_config(
    page_title="AI Cloud Resource Optimization Copilot",
    page_icon="☁️",
    layout="wide"
)

# ==========================================================
# HERO SECTION
# ==========================================================

st.title("☁️ AI Cloud Resource Optimization Copilot")

st.markdown(
    """
### Predict • Optimize • Prevent

An AI-powered assistant that analyzes Google Cloud resources using
Large Language Models to predict capacity bottlenecks, recommend
cost optimizations, and answer cloud operations questions.
"""
)

st.divider()

# ==========================================================
# FEATURES
# ==========================================================

st.subheader("🚀 Platform Capabilities")

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.markdown("## 📊 Cloud Monitoring")

        st.write("""
Monitor Google Cloud resources including:

- BigQuery
- Dataproc
- Dataflow
- Cloud Storage
""")

    with st.container(border=True):

        st.markdown("## 💬 AI Copilot")

        st.write("""
Ask natural language questions about your
cloud environment and receive AI-powered
answers.
""")

with col2:

    with st.container(border=True):

        st.markdown("## 🧠 AI Cloud Architect")

        st.write("""
Gemini analyzes historical metrics to:

- Predict capacity issues
- Explain reasoning
- Recommend optimizations
- Estimate business impact
""")

    with st.container(border=True):

        st.markdown("## 💰 FinOps Insights")

        st.write("""
Identify opportunities to:

- Reduce cloud costs
- Optimize resource utilization
- Improve operational efficiency
""")

st.divider()

# ==========================================================
# ARCHITECTURE
# ==========================================================

# st.subheader("🏗️ AI Architecture")

# st.code(
# """
# Google Cloud Metrics
#         │
#         ▼
# Historical Cloud Metrics
#         │
#         ▼
# Context Builder
#         │
#         ▼
# Prompt Builder
#         │
#         ▼
# Gemini LLM
#         │
#         ▼
# Prediction + Recommendation + Reasoning
#         │
#         ▼
# Streamlit Dashboard
# """,
# language="text"
# )

# st.divider()

# ==========================================================
# SYSTEM STATUS
# ==========================================================

st.subheader("🟢 System Status")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("Backend Connected")

with c2:
    st.success("Gemini Connected")

with c3:
    st.success("Mock GCP Provider")

st.divider()

st.caption(
    "🚀 Powered by FastAPI • Streamlit • Gemini AI • Google Cloud"
)
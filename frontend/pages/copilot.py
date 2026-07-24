import streamlit as st

from services.api_client import APIClient

st.set_page_config(
    page_title="AI Copilot",
    layout="wide"
)

st.title("💬 AI Cloud Copilot")

st.caption(
    "Ask questions about your Google Cloud environment."
)

question = st.text_area(
    "Ask your question",
    placeholder="Why is BigQuery utilization so high?"
)

if st.button("Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("🧠 Thinking..."):

        answer = APIClient.ask_copilot(question)

    st.success(answer)

#-------------footer-----------------    

st.divider()

st.caption(
    "🚀 Cloud Resource Optimization Copilot | FastAPI | Streamlit | Gemini AI | Google Cloud"
)
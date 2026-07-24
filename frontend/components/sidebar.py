"""
Application Sidebar
"""

import streamlit as st


def render_sidebar():

    st.sidebar.title("☁ Cloud Copilot")

    st.sidebar.success("Backend Connected")

    st.sidebar.markdown("---")

    st.sidebar.write("Version")

    st.sidebar.caption("1.0.0")
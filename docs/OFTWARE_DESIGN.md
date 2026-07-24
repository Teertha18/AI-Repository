# AI Cloud Resource Optimization Copilot

## Version
0.1

## Project Vision

Build an AI-powered Cloud Resource Optimization Copilot that helps cloud engineers:

- Monitor cloud resources
- Predict future resource demand
- Detect inefficiencies
- Explain optimization opportunities using AI
- Recommend cost-saving actions
- Execute approved actions safely

---

# Problem Statement

Cloud environments grow rapidly, making manual monitoring difficult.

Engineers spend significant time:
- Analyzing cloud costs
- Investigating resource utilization
- Planning capacity
- Identifying optimization opportunities

Our application acts as an AI Copilot that performs these investigations automatically.

---

# Target Users

- Cloud Engineers
- DevOps Engineers
- FinOps Teams
- Site Reliability Engineers
- Platform Engineers

---

# Functional Requirements

### Dashboard
Display:

- Monthly Spend
- Potential Savings
- Average CPU Utilization
- Active Recommendations

---

### Forecasting

Predict future utilization using historical metrics.

---

### AI Copilot

Allow users to ask natural language questions such as:

- Why is my cloud bill increasing?
- Which VM is underutilized?
- Can I reduce Compute Engine costs?

---

### Recommendations

Display:

- Resource
- Recommendation
- Estimated Savings
- Confidence Score
- Risk Level
- Explanation

---

### Auto Scaling

Allow users to:

- Approve
- Reject
- Schedule
- Execute

AI recommendations.

---

### History

Display executed recommendations and actions.

---

# Non Functional Requirements

- Responsive UI
- Modular Architecture
- Secure configuration
- Extensible design
- Logging
- Error handling

---

# Technology Stack

Frontend:
- Streamlit

Backend:
- Python

AI:
- Gemini

Visualization:
- Plotly

Cloud:
- Google Cloud Platform

Storage:
- SQLite (initially)

Deployment:
- Cloud Run
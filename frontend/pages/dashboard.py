import streamlit as st

from services.api_client import APIClient

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
)

# -------------------------------------------------------
# Page Header
# -------------------------------------------------------

st.title("📊 Cloud Resource Dashboard")

st.caption(
    "Real-time monitoring of Google Cloud Platform resources."
)

st.divider()

# -------------------------------------------------------
# Fetch Metrics
# -------------------------------------------------------

try:
    data = APIClient.get_metrics()

except Exception as e:
    st.error(f"Unable to fetch metrics.\n\n{e}")
    st.stop()

# -------------------------------------------------------
# Helper Functions
# -------------------------------------------------------

def get_health(utilization):

    if utilization >= 90:
        return "🔴 Critical"

    elif utilization >= 75:
        return "🟡 Warning"

    return "🟢 Healthy"


def service_card(
    title,
    icon,
    utilization,
    metrics,
    ai_status
):

    with st.container(border=True):

        st.subheader(f"{icon} {title}")

        health = get_health(utilization)

        st.metric(
            "Health",
            health
        )

        st.metric(
            "Utilization",
            f"{utilization:.1f}%"
        )

        st.progress(utilization / 100)

        st.divider()

        for key, value in metrics.items():
            st.write(f"**{key}:** {value}")

        st.divider()

        st.info(ai_status)


# -------------------------------------------------------
# Calculate Utilization
# -------------------------------------------------------

bq = data["bigquery"]
dp = data["dataproc"]
df = data["dataflow"]
gcs = data["gcs"]

bq_util = (bq["used_slots"] / bq["reserved_slots"]) * 100

dp_util = (dp["active_clusters"] / dp["clusters"]) * 100

df_util = (df["used_workers"] / df["max_workers"]) * 100

# GCS doesn't have utilization
gcs_health = "🟢 Healthy"

# -------------------------------------------------------
# Overall Health
# -------------------------------------------------------

critical = 0
warning = 0
healthy = 0

for util in [bq_util, dp_util, df_util]:

    if util >= 90:
        critical += 1

    elif util >= 75:
        warning += 1

    else:
        healthy += 1

healthy += 1  # GCS

overall = "⚠ Needs Attention" if critical else "✅ Healthy"

st.subheader("Overall Cloud Health")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🔴 Critical",
        critical
    )

with c2:
    st.metric(
        "🟡 Warning",
        warning
    )

with c3:
    st.metric(
        "🟢 Healthy",
        healthy
    )

with c4:
    st.metric(
        "Overall",
        overall
    )

st.divider()

# -------------------------------------------------------
# Service Cards
# -------------------------------------------------------

left, right = st.columns(2)

# -------------------------------------------------------
# BigQuery
# -------------------------------------------------------

with left:

    service_card(
        title="BigQuery",
        icon="🟦",
        utilization=bq_util,
        metrics={
            "Reserved Slots": bq["reserved_slots"],
            "Used Slots": bq["used_slots"],
        },
        ai_status="Capacity exhausted. AI recommends increasing slot reservations."
    )

# -------------------------------------------------------
# Dataproc
# -------------------------------------------------------

with right:

    service_card(
        title="Dataproc",
        icon="🟩",
        utilization=dp_util,
        metrics={
            "Clusters": dp["clusters"],
            "Active Clusters": dp["active_clusters"],
        },
        ai_status="All clusters are active. Consider autoscaling."
    )

# -------------------------------------------------------
# Dataflow
# -------------------------------------------------------

with left:

    service_card(
        title="Dataflow",
        icon="🟨",
        utilization=df_util,
        metrics={
            "Workers": df["used_workers"],
            "Max Workers": df["max_workers"],
        },
        ai_status="Worker utilization is increasing. Monitor scaling."
    )

# -------------------------------------------------------
# Cloud Storage
# -------------------------------------------------------

with right:

    with st.container(border=True):

        st.subheader("🟪 Cloud Storage")

        st.metric(
            "Health",
            gcs_health
        )

        st.metric(
            "Storage",
            f'{gcs["storage_tb"]} TB'
        )

        if "growth_percentage" in gcs:
            st.metric(
                "Daily Growth",
                f'{gcs["growth_percentage"]}%'
            )

        st.divider()

        st.info(
            "Storage growth is healthy. Continue lifecycle policy optimization."
        )

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.divider()

st.caption(
    "🚀 AI Cloud Resource Optimization Copilot | FastAPI • Gemini AI • Streamlit • Google Cloud"
)
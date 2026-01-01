import streamlit as st
import pandas as pd
import requests
from PIL import Image

# =========================
# Page Config (Title + Icon)
# =========================
logo = Image.open("assests/logo0.png")

st.set_page_config(
    page_title="ICS/OT Network Detection & Response",
    page_icon=logo,
    layout="wide"
)

# =========================
# Custom Styling
# =========================
st.markdown("""
<style>
    body {
        background-color: #0B1220;
    }
    .block-container {
        padding-top: 2rem;
    }
    h1, h2, h3 {
        color: #E5E7EB;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# Header Section
# =========================
col1, col2 = st.columns([1, 6])

with col1:
    st.image("assests/logo0.png", width=120)

with col2:
    st.markdown("""
    <h1 style='margin-bottom: 0;'>ICS/OT Network Detection & Response</h1>
    <p style='color:#9CA3AF; font-size:16px;'>
    ML-Based Anomaly & Attack Detection for Industrial Networks
    </p>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================
# Backend Configuration
# =========================
BACKEND_URL = "http://127.0.0.1:5000/predict"

REQUIRED_FEATURES = [
    "flow_durat",
    "pkts_toserver",
    "pkts_toclient",
    "bytes_toserver",
    "bytes_toclient",
    "src_port",
    "dst_port"
]

# =========================
# Sidebar
# =========================
st.sidebar.header("⚙️ Input Options")
uploaded_file = st.sidebar.file_uploader(
    "Upload Flow-Level CSV File",
    type=["csv"]
)

# =========================
# Main Logic
# =========================
if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Uploaded Data Preview")
    st.dataframe(df.head())

    # ---- Validate Columns
    missing_cols = [c for c in REQUIRED_FEATURES if c not in df.columns]
    if missing_cols:
        st.error(f"❌ Missing required columns: {missing_cols}")
        st.stop()

    if st.button("🚨 Analyze Traffic"):

        results = []

        with st.spinner("Analyzing traffic using ML models..."):
            for _, row in df.iterrows():
                payload = {f: float(row[f]) for f in REQUIRED_FEATURES}

                try:
                    response = requests.post(BACKEND_URL, json=payload, timeout=5)
                    result = response.json()["prediction"]
                    results.append(result["label"])
                except Exception:
                    results.append("error")

        df["prediction"] = results

        # =========================
        # Results Section
        # =========================
        st.markdown("---")
        st.subheader("📊 Detection Results")

        colA, colB, colC = st.columns(3)

        with colA:
            st.metric("Normal Flows", (df["prediction"] == "normal").sum())

        with colB:
            st.metric("Scan Detected", (df["prediction"] == "scan").sum())

        with colC:
            st.metric("Attacks Detected", (df["prediction"] == "attack").sum())

        st.markdown("---")
        st.subheader("📌 Detailed Results")
        st.dataframe(df)

        # =========================
        # Alerts
        # =========================
        if (df["prediction"] == "attack").any():
            st.error("🚨 Critical Alert: Real ATTACK detected in network traffic!")

        elif (df["prediction"] == "scan").any():
            st.warning("⚠️ Warning: Network scanning activity detected.")

        else:
            st.success("✅ Network traffic appears NORMAL.")

else:
    st.info("⬅️ Please upload a CSV file containing flow-level features to start analysis.")

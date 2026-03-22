import streamlit as st
import pickle
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ============================================================
# LOAD
# ============================================================
model  = pickle.load(open("model.pkl",  "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="wide")

# ============================================================
# CSS
# ============================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    * { font-family: 'Inter', sans-serif; }

    .stApp { background-color: #0a0a0f; }

    section[data-testid="stSidebar"] { display: none; }

    /* header */
    .header-container {
        background: linear-gradient(135deg, #0f0f1a 0%, #1a0533 50%, #0f0f1a 100%);
        border: 1px solid #2d1b69;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin-bottom: 30px;
    }
    .header-badge {
        background: linear-gradient(135deg, #6c63ff, #a855f7);
        color: white;
        padding: 6px 18px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 15px;
        letter-spacing: 1px;
    }
    .header-title {
        font-size: 52px;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        line-height: 1.2;
    }
    .header-subtitle {
        color: #6b7280;
        font-size: 16px;
        margin-top: 10px;
    }

    /* cards */
    .card {
        background: #111118;
        border: 1px solid #1f1f2e;
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
    }
    .card-title {
        font-size: 13px;
        font-weight: 600;
        color: #6c63ff;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 20px;
    }

    /* inputs */
    .stNumberInput input {
        background-color: #1a1a2e !important;
        color: #ffffff !important;
        border: 1px solid #2d2d4e !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-size: 15px !important;
    }
    .stNumberInput input:focus {
        border-color: #6c63ff !important;
        box-shadow: 0 0 0 2px rgba(108,99,255,0.2) !important;
    }
    .stNumberInput label {
        color: #9ca3af !important;
        font-size: 13px !important;
        font-weight: 500 !important;
    }

    /* button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #6c63ff, #a855f7) !important;
        color: white !important;
        border: none !important;
        padding: 16px !important;
        border-radius: 12px !important;
        font-size: 17px !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        transition: all 0.3s !important;
        margin-top: 10px !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 30px rgba(108,99,255,0.4) !important;
    }

    /* result */
    .result-container {
        background: linear-gradient(135deg, #0f0f1a, #1a0533);
        border: 1px solid #6c63ff;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 0 40px rgba(108,99,255,0.15);
    }
    .result-label {
        color: #9ca3af;
        font-size: 14px;
        font-weight: 500;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    .result-price {
        font-size: 58px;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.1;
    }
    .result-sub {
        color: #6b7280;
        font-size: 14px;
        margin-top: 10px;
    }

    /* metric cards */
    [data-testid="stMetric"] {
        background: #111118 !important;
        border: 1px solid #1f1f2e !important;
        border-radius: 12px !important;
        padding: 20px !important;
    }
    [data-testid="stMetricLabel"] { color: #9ca3af !important; font-size: 12px !important; }
    [data-testid="stMetricValue"] { color: #ffffff !important; font-size: 22px !important; font-weight: 700 !important; }

    /* divider */
    hr { border-color: #1f1f2e !important; }

    /* text */
    p, div, label { color: #ffffff !important; }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================
st.markdown("""
    <div class="header-container">
        <div class="header-badge">🏠 AI POWERED</div>
        <p class="header-title">House Price Predictor</p>
        <p class="header-subtitle">Get instant price estimates powered by Machine Learning</p>
    </div>
""", unsafe_allow_html=True)

# ============================================================
# STATS ROW
# ============================================================
s1, s2, s3, s4 = st.columns(4)
s1.metric("Model",      "Linear Regression")
s2.metric("R² Score",   "0.91")
s3.metric("MAE",        "$80,859")
s4.metric("Dataset",    "5,000 Houses")

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# MAIN LAYOUT
# ============================================================
left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown('<div class="card"><p class="card-title">📍 Location & Area</p>', unsafe_allow_html=True)
    income     = st.number_input("💰 Avg Area Income ($)",     min_value=0.0,   value=68000.0,  step=1000.0)
    population = st.number_input("👥 Area Population",         min_value=0.0,   value=36000.0,  step=500.0)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card"><p class="card-title">🏚️ Property Details</p>', unsafe_allow_html=True)
    age        = st.number_input("📅 Avg House Age (years)",   min_value=1.0,   value=5.97,     step=0.1)
    rooms      = st.number_input("🛋️  Avg Number of Rooms",    min_value=1.0,   value=6.98,     step=0.1)
    bedrooms   = st.number_input("🛏️  Avg Number of Bedrooms", min_value=1.0,   value=3.98,     step=0.1)
    st.markdown('</div>', unsafe_allow_html=True)

    predict_btn = st.button("🔍 Predict House Price")

with right:
    if predict_btn:
        input_data   = np.array([[income, age, rooms, bedrooms, population]])
        input_scaled = scaler.transform(input_data)
        prediction   = model.predict(input_scaled)[0]

        # result box
        st.markdown(f"""
            <div class="result-container">
                <p class="result-label">Estimated House Price</p>
                <p class="result-price">${prediction:,.0f}</p>
                <p class="result-sub">Based on current market conditions</p>
            </div>
        """, unsafe_allow_html=True)

        # range metrics
        c1, c2, c3 = st.columns(3)
        c1.metric("🔻 Min Estimate", f"${prediction*0.90:,.0f}")
        c2.metric("🎯 Predicted",    f"${prediction:,.0f}")
        c3.metric("🔺 Max Estimate", f"${prediction*1.10:,.0f}")

        st.markdown("<br>", unsafe_allow_html=True)

        # gauge chart
        fig_gauge = go.Figure(go.Indicator(
            mode  = "gauge+number",
            value = prediction,
            title = {"text": "Price Estimate", "font": {"color": "white", "size": 14}},
            number = {"prefix": "$", "font": {"color": "white", "size": 28}},
            gauge = {
                "axis"  : {"range": [500000, 2500000], "tickcolor": "white"},
                "bar"   : {"color": "#6c63ff"},
                "bgcolor": "#1a1a2e",
                "steps" : [
                    {"range": [500000,  1000000], "color": "#1a1a2e"},
                    {"range": [1000000, 1700000], "color": "#16213e"},
                    {"range": [1700000, 2500000], "color": "#0f3460"},
                ],
                "threshold": {
                    "line" : {"color": "#a855f7", "width": 4},
                    "value": prediction
                }
            }
        ))
        fig_gauge.update_layout(
            paper_bgcolor="#0a0a0f",
            plot_bgcolor ="#0a0a0f",
            font_color   ="white",
            height       = 280,
            margin       = dict(t=40, b=10, l=20, r=20)
        )
        st.plotly_chart(fig_gauge, use_container_width=True)

        # feature impact bar chart
        feature_names  = ["Area Income", "House Age", "Num Rooms", "Bedrooms", "Population"]
        feature_values = [income, age, rooms, bedrooms, population]
        colors         = ["#6c63ff", "#a855f7", "#ec4899", "#f59e0b", "#10b981"]

        fig_bar = go.Figure(go.Bar(
            x           = feature_names,
            y           = feature_values,
            marker_color= colors,
            text        = [f"{v:,.1f}" for v in feature_values],
            textposition= "outside",
            textfont    = {"color": "white"}
        ))
        fig_bar.update_layout(
            title       = "Your Input Features",
            paper_bgcolor="#0a0a0f",
            plot_bgcolor = "#111118",
            font_color  = "white",
            height      = 300,
            margin      = dict(t=50, b=20, l=20, r=20),
            xaxis       = dict(showgrid=False),
            yaxis       = dict(showgrid=True, gridcolor="#1f1f2e")
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    else:
        st.markdown("""
            <div style="height:400px; display:flex; flex-direction:column;
                        align-items:center; justify-content:center;
                        border: 2px dashed #2d2d4e; border-radius:20px;">
                <p style="font-size:60px; margin:0;">🏠</p>
                <p style="color:#6b7280; font-size:16px; margin-top:15px;">
                    Fill in the details and click Predict
                </p>
            </div>
        """, unsafe_allow_html=True)

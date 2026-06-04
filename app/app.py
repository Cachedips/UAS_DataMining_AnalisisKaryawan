import streamlit as st

st.set_page_config(
    page_title="IBM HR Attrition Analytics",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
/* Sidebar background */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #0f2640 0%, #1a3d6b 100%);
}
[data-testid="stSidebar"] * { color: #e8f0fe !important; }

/* Metric cards */
div[data-testid="metric-container"] {
    background: #f0f6ff;
    border: 1px solid #c8deff;
    border-radius: 12px;
    padding: 16px;
}

/* Tombol utama */
div.stButton > button {
    background: linear-gradient(135deg, #185FA5, #1D9E75);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 28px;
    font-size: 15px;
    font-weight: 600;
    transition: opacity 0.2s;
}
div.stButton > button:hover { opacity: 0.85; }

/* Card container */
.card {
    background: white;
    border-radius: 14px;
    padding: 24px;
    border: 1px solid #e3eaf5;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    margin-bottom: 16px;
}

/* Badge pills */
.badge {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    margin: 3px;
}
.badge-blue  { background:#dbeafe; color:#1e40af; }
.badge-green { background:#dcfce7; color:#166534; }
.badge-red   { background:#fee2e2; color:#991b1b; }
.badge-amber { background:#fef3c7; color:#92400e; }

/* Section header */
.section-header {
    font-size: 22px;
    font-weight: 700;
    color: #0f2640;
    border-left: 5px solid #1D9E75;
    padding-left: 14px;
    margin: 24px 0 16px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 20px 0 10px;'>
        <div style='font-size:48px;'>🏢</div>
        <div style='font-size:18px; font-weight:700; margin-top:8px;'>IBM HR Analytics</div>
        <div style='font-size:12px; opacity:0.75; margin-top:4px;'>Attrition Prediction System</div>
    </div>
    <hr style='border-color:rgba(255,255,255,0.15); margin:12px 0;'>
    """, unsafe_allow_html=True)

    st.markdown("**📌 Navigasi**")
    st.info("Gunakan menu di atas untuk berpindah halaman.")

    st.markdown("""
    <hr style='border-color:rgba(255,255,255,0.15); margin:12px 0;'>
    <div style='font-size:11px; opacity:0.6; text-align:center;'>
        UAS Data Mining · 2024/2025<br>
        Framework: CRISP-DM
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; padding: 60px 20px;'>
    <div style='font-size:64px;'>🏢</div>
    <h1 style='font-size:36px; font-weight:800; color:#0f2640; margin:16px 0 8px;'>
        IBM HR Analytics
    </h1>
    <p style='font-size:18px; color:#64748b; max-width:520px; margin:0 auto;'>
        Sistem Prediksi & Analisis Risiko Attrition Karyawan
    </p>
    <div style='margin-top:24px;'>
        <span class='badge badge-blue'>XGBoost Classification</span>
        <span class='badge badge-green'>K-Means Clustering</span>
        <span class='badge badge-amber'>SHAP Explainable AI</span>
        <span class='badge badge-red'>CRISP-DM</span>
    </div>
    <p style='font-size:14px; color:#94a3b8; margin-top:32px;'>
        ← Pilih halaman dari sidebar kiri untuk memulai
    </p>
</div>
""", unsafe_allow_html=True)

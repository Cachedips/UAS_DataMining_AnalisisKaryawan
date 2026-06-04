import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os, sys
import plotly.graph_objects as go
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from assets.style import inject_css

st.set_page_config(page_title="Prediksi Attrition", page_icon="🤖", layout="wide")
inject_css()

# Extra CSS halaman ini
st.markdown("""
<style>
.result-resign {
    background: linear-gradient(135deg,#fee2e2,#fecaca);
    border: 2px solid #E24B4A; border-radius: 18px;
    padding: 32px 24px; text-align:center;
    box-shadow: 0 8px 28px rgba(226,75,74,0.2);
    animation: pulse-red 2s infinite;
}
@keyframes pulse-red {
    0%,100%{ box-shadow:0 8px 28px rgba(226,75,74,0.2); }
    50%    { box-shadow:0 8px 36px rgba(226,75,74,0.4); }
}
.result-safe {
    background: linear-gradient(135deg,#dcfce7,#bbf7d0);
    border: 2px solid #1D9E75; border-radius: 18px;
    padding: 32px 24px; text-align:center;
    box-shadow: 0 8px 28px rgba(29,158,117,0.2);
    animation: pulse-green 2s infinite;
}
@keyframes pulse-green {
    0%,100%{ box-shadow:0 8px 28px rgba(29,158,117,0.2); }
    50%    { box-shadow:0 8px 36px rgba(29,158,117,0.4); }
}
.cluster-card {
    background: white; border-radius:16px; padding:22px;
    border:1px solid rgba(99,179,237,0.25);
    box-shadow:0 4px 20px rgba(13,31,62,0.08);
    transition: all 0.3s ease;
}
.cluster-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 36px rgba(13,31,62,0.14);
}
.rec-item {
    padding:10px 14px; background:#f0f7ff; border-radius:10px;
    margin:6px 0; font-size:13px; border-left:3px solid #185FA5;
    transition: all 0.2s ease;
}
.rec-item:hover {
    background:#dbeafe; transform:translateX(4px);
    border-left-color:#1D9E75;
}
div.stForm { background:white; border-radius:18px; padding:24px; border:1px solid rgba(99,179,237,0.2); }
div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg,#0d1f3e,#185FA5) !important;
    color:white !important; border:none !important; border-radius:12px !important;
    padding:14px 28px !important; font-size:16px !important; font-weight:700 !important;
    width:100% !important; transition:all 0.25s ease !important;
    box-shadow:0 6px 20px rgba(24,95,165,0.4) !important;
}
div[data-testid="stFormSubmitButton"] > button:hover {
    transform:translateY(-2px) !important;
    box-shadow:0 10px 30px rgba(24,95,165,0.55) !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='page-header'>
    <h1>🤖 Prediksi Risiko Attrition</h1>
    <p>Masukkan data karyawan untuk mendapatkan prediksi risiko resign dan pengelompokan cluster</p>
</div>
""", unsafe_allow_html=True)

# ── Load model ─────────────────────────────────────────────────────────────────
@st.cache_resource
def load_models():
    for base in ["../model", "model"]:
        try:
            return (
                joblib.load(f"{base}/xgb_model.pkl"),
                joblib.load(f"{base}/kmeans_model.pkl"),
                joblib.load(f"{base}/scaler.pkl"),
                joblib.load(f"{base}/encoders.pkl"),
                joblib.load(f"{base}/feature_names.pkl"),
                joblib.load(f"{base}/cluster_features.pkl"),
            )
        except Exception:
            continue
    return None

models = load_models()
if models is None:
    st.error("⚠️ Model tidak ditemukan. Jalankan notebook terlebih dahulu.")
    st.stop()

xgb_model, kmeans_model, scaler, encoders, feature_names, cluster_features = models

CLUSTER_INFO = {
    0: {"name": "Karyawan Loyal & Puas",    "color": "#1D9E75", "bg": "#dcfce7", "risk": "Rendah",  "emoji": "🟢"},
    1: {"name": "Karyawan Berisiko Sedang", "color": "#BA7517", "bg": "#fef3c7", "risk": "Sedang",  "emoji": "🟡"},
    2: {"name": "Karyawan Burnout",         "color": "#E24B4A", "bg": "#fee2e2", "risk": "Tinggi",  "emoji": "🔴"},
    3: {"name": "Karyawan Potensial",       "color": "#185FA5", "bg": "#dbeafe", "risk": "Rendah",  "emoji": "🔵"},
}

# ── FORM ───────────────────────────────────────────────────────────────────────
st.markdown("### 📝 Form Data Karyawan")
st.markdown("""
<div style='background:linear-gradient(135deg,#e8f2ff,#dbeafe); border-radius:12px;
            padding:12px 18px; font-size:13px; color:#1e40af; margin-bottom:16px;
            border-left:4px solid #185FA5;'>
    💡 Isi semua data karyawan di bawah, lalu klik <b>🔍 Proses Prediksi</b>
</div>
""", unsafe_allow_html=True)

with st.form("prediction_form"):
    # Demografis
    st.markdown("#### 👤 Data Demografis")
    c1,c2,c3,c4 = st.columns(4)
    age          = c1.slider("Usia", 18, 60, 35)
    gender       = c2.selectbox("Jenis Kelamin", ["Male","Female"])
    marital      = c3.selectbox("Status Pernikahan", ["Single","Married","Divorced"])
    dist_home    = c4.slider("Jarak Rumah (km)", 1, 29, 10)

    # Pekerjaan
    st.markdown("#### 💼 Data Pekerjaan")
    c1,c2,c3,c4 = st.columns(4)
    department   = c1.selectbox("Departemen", ["Sales","Research & Development","Human Resources"])
    job_role     = c2.selectbox("Jabatan", [
        "Sales Executive","Research Scientist","Laboratory Technician",
        "Manufacturing Director","Healthcare Representative","Manager",
        "Sales Representative","Research Director","Human Resources"])
    job_level    = c3.slider("Level Jabatan", 1, 5, 2)
    biz_travel   = c4.selectbox("Perjalanan Bisnis", ["Non-Travel","Travel_Rarely","Travel_Frequently"])

    # Finansial
    st.markdown("#### 💰 Data Finansial & Pengalaman")
    c1,c2,c3,c4 = st.columns(4)
    monthly_income  = c1.number_input("Gaji Bulanan ($)", 1009, 19999, 5000, step=500)
    daily_rate      = c2.slider("Daily Rate", 102, 1499, 800)
    hourly_rate     = c3.slider("Hourly Rate", 30, 100, 65)
    monthly_rate    = c4.slider("Monthly Rate", 2094, 26999, 14000, step=500)

    c1,c2,c3,c4 = st.columns(4)
    total_working   = c1.slider("Total Tahun Bekerja", 0, 40, 10)
    years_company   = c2.slider("Tahun di Perusahaan", 0, 40, 5)
    years_role      = c3.slider("Tahun di Jabatan", 0, 18, 3)
    years_manager   = c4.slider("Tahun dg Manager", 0, 17, 2)

    c1,c2,c3 = st.columns(3)
    num_companies   = c1.slider("Jumlah Perusahaan Sblmnya", 0, 9, 2)
    years_promo     = c2.slider("Tahun Sejak Promosi", 0, 15, 2)
    training_last   = c3.slider("Training Tahun Lalu (x)", 0, 6, 2)

    # Kepuasan
    st.markdown("#### ⭐ Kepuasan & Performa")
    c1,c2,c3,c4 = st.columns(4)
    job_satisfaction = c1.slider("Kepuasan Kerja (1-4)", 1, 4, 3)
    env_satisfaction = c2.slider("Kepuasan Lingkungan (1-4)", 1, 4, 3)
    rel_satisfaction = c3.slider("Kepuasan Hubungan (1-4)", 1, 4, 3)
    work_life        = c4.slider("Work-Life Balance (1-4)", 1, 4, 3)

    c1,c2,c3,c4 = st.columns(4)
    job_involvement  = c1.slider("Keterlibatan Kerja (1-4)", 1, 4, 3)
    performance      = c2.slider("Performa Rating (1-4)", 1, 4, 3)
    education        = c3.slider("Pendidikan (1-5)", 1, 5, 3)
    edu_field        = c4.selectbox("Bidang Pendidikan", [
        "Life Sciences","Other","Medical","Marketing","Technical Degree","Human Resources"])

    c1,c2 = st.columns(2)
    overtime         = c1.selectbox("Overtime (Lembur)", ["Yes","No"])
    stock_option     = c2.slider("Stock Option Level (0-3)", 0, 3, 1)

    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🔍 Proses Prediksi", use_container_width=True)

# ── HASIL ──────────────────────────────────────────────────────────────────────
if submitted:
    input_dict = {
        'Age': age, 'BusinessTravel': biz_travel, 'DailyRate': daily_rate,
        'Department': department, 'DistanceFromHome': dist_home,
        'Education': education, 'EducationField': edu_field,
        'EnvironmentSatisfaction': env_satisfaction, 'Gender': gender,
        'HourlyRate': hourly_rate, 'JobInvolvement': job_involvement,
        'JobLevel': job_level, 'JobRole': job_role,
        'JobSatisfaction': job_satisfaction, 'MaritalStatus': marital,
        'MonthlyIncome': monthly_income, 'MonthlyRate': monthly_rate,
        'NumCompaniesWorked': num_companies, 'OverTime': overtime,
        'PercentSalaryHike': 14, 'PerformanceRating': performance,
        'RelationshipSatisfaction': rel_satisfaction, 'StockOptionLevel': stock_option,
        'TotalWorkingYears': total_working, 'TrainingTimesLastYear': training_last,
        'WorkLifeBalance': work_life, 'YearsAtCompany': years_company,
        'YearsInCurrentRole': years_role, 'YearsSinceLastPromotion': years_promo,
        'YearsWithCurrManager': years_manager,
    }

    input_df = pd.DataFrame([input_dict])
    for col, le in encoders.items():
        if col in input_df.columns and col != 'Attrition':
            try:
                input_df[col] = le.transform(input_df[col])
            except ValueError:
                input_df[col] = 0

    for col in feature_names:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[feature_names]

    pred        = xgb_model.predict(input_df)[0]
    pred_proba  = xgb_model.predict_proba(input_df)[0]
    resign_prob = pred_proba[1] * 100
    safe_prob   = pred_proba[0] * 100

    # Clustering
    cluster_input = {f: input_dict.get(f, 0) for f in cluster_features}
    cluster_df    = pd.DataFrame([cluster_input])
    for col, le in encoders.items():
        if col in cluster_df.columns:
            try:
                cluster_df[col] = le.transform(cluster_df[col])
            except Exception:
                cluster_df[col] = 0
    cluster_scaled = scaler.transform(cluster_df)
    cluster_label  = kmeans_model.predict(cluster_scaled)[0]
    ci             = CLUSTER_INFO.get(cluster_label, CLUSTER_INFO[0])

    st.markdown("---")
    st.markdown("## 📊 Hasil Prediksi")

    col_r, col_c = st.columns(2, gap="large")

    with col_r:
        st.markdown("### 🎯 Model 1 — XGBoost Classification")
        if pred == 1:
            st.markdown(f"""
            <div class='result-resign'>
                <div style='font-size:54px;'>⚠️</div>
                <h2 style='color:#991b1b; margin:10px 0 6px; font-size:26px; font-weight:800;'>
                    BERISIKO RESIGN
                </h2>
                <p style='color:#7f1d1d; font-size:14px; margin:0 0 14px;'>
                    Karyawan ini diprediksi akan meninggalkan perusahaan
                </p>
                <div style='font-size:42px; font-weight:900; color:#E24B4A;'>{resign_prob:.1f}%</div>
                <div style='font-size:13px; color:#7f1d1d; margin-top:4px;'>Probabilitas Resign</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='result-safe'>
                <div style='font-size:54px;'>✅</div>
                <h2 style='color:#166534; margin:10px 0 6px; font-size:26px; font-weight:800;'>
                    AMAN · TIDAK RESIGN
                </h2>
                <p style='color:#14532d; font-size:14px; margin:0 0 14px;'>
                    Karyawan ini diprediksi tetap bertahan di perusahaan
                </p>
                <div style='font-size:42px; font-weight:900; color:#1D9E75;'>{safe_prob:.1f}%</div>
                <div style='font-size:13px; color:#14532d; margin-top:4px;'>Probabilitas Tidak Resign</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=resign_prob,
            domain={'x':[0,1],'y':[0,1]},
            title={'text':"Probabilitas Resign (%)",'font':{'size':14,'color':'#0d1f3e'}},
            number={'suffix':'%','font':{'color':'#185FA5','size':36}},
            gauge={
                'axis':{'range':[0,100],'tickwidth':1,'tickcolor':'#94a3b8'},
                'bar':{'color':'#E24B4A' if resign_prob>50 else '#1D9E75','thickness':0.25},
                'bgcolor':"white",
                'borderwidth':2, 'bordercolor':'#e3eaf5',
                'steps':[
                    {'range':[0,30], 'color':'#dcfce7'},
                    {'range':[30,60],'color':'#fef3c7'},
                    {'range':[60,100],'color':'#fee2e2'},
                ],
                'threshold':{'line':{'color':'#0d1f3e','width':3},'thickness':0.75,'value':50}
            }
        ))
        fig_gauge.update_layout(height=280, margin=dict(t=40,b=10,l=20,r=20),
                                 paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col_c:
        st.markdown("### 🔵 Model 2 — K-Means Clustering")
        st.markdown(f"""
        <div class='cluster-card' style='border-left:5px solid {ci["color"]};
                    background:linear-gradient(135deg,white,{ci["bg"]}22);'>
            <div style='font-size:40px; margin-bottom:10px;'>{ci["emoji"]}</div>
            <div style='font-size:12px; color:#64748b; letter-spacing:0.05em; text-transform:uppercase;'>
                Cluster {cluster_label}
            </div>
            <div style='font-size:22px; font-weight:800; color:{ci["color"]}; margin:6px 0 12px;'>
                {ci["name"]}
            </div>
            <div style='background:{ci["bg"]}; border-radius:10px; padding:10px 16px;
                        font-size:13px; color:#374151; display:inline-block;'>
                <b>Tingkat Risiko:</b>
                <span style='color:{ci["color"]}; font-weight:700;'>{ci["risk"]}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Donut
        distances    = np.linalg.norm(kmeans_model.cluster_centers_ - cluster_scaled, axis=1)
        inv_dist     = 1/(distances+1e-6)
        proba_cluster= inv_dist/inv_dist.sum()*100

        fig_donut = go.Figure(go.Pie(
            labels=[f"C{i}: {CLUSTER_INFO[i]['name']}" for i in range(4)],
            values=proba_cluster.round(2),
            hole=0.58,
            marker_colors=[CLUSTER_INFO[i]['color'] for i in range(4)],
            pull=[0.1 if i==cluster_label else 0 for i in range(4)]
        ))
        fig_donut.update_traces(textinfo='percent', textfont_size=12)
        fig_donut.update_layout(
            title='Kedekatan ke Tiap Cluster', height=290,
            margin=dict(t=40,b=10,l=10,r=10),
            showlegend=True,
            legend=dict(font_size=10, orientation='h', y=-0.15),
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_donut, use_container_width=True)

        st.markdown("#### 💡 Rekomendasi Aksi HR")
        if pred==1 and ci['risk']=='Tinggi':
            recs = ["🚨 Jadwalkan 1-on-1 segera dengan manajer",
                    "💰 Tinjau ulang kompensasi & benefit",
                    "⏰ Evaluasi beban kerja dan overtime",
                    "🎯 Berikan project yang lebih menantang"]
        elif pred==1:
            recs = ["📋 Lakukan exit interview preventif",
                    "🔄 Pertimbangkan rotasi departemen",
                    "📈 Rencanakan jalur karir yang jelas"]
        else:
            recs = ["✅ Pertahankan kondisi kerja yang baik",
                    "🏆 Berikan apresiasi & recognition rutin",
                    "📚 Investasi pada pengembangan skill"]

        for r in recs:
            st.markdown(f"<div class='rec-item'>{r}</div>", unsafe_allow_html=True)

    with st.expander("📋 Lihat Ringkasan Data Input"):
        summary = {
            'Usia': age, 'Gender': gender, 'Status': marital,
            'Departemen': department, 'Jabatan': job_role,
            'Gaji Bulanan': f"${monthly_income:,}",
            'Total Pengalaman': f"{total_working} tahun",
            'Tahun di Perusahaan': f"{years_company} tahun",
            'Overtime': overtime,
            'Kepuasan Kerja': f"{job_satisfaction}/4",
            'Work-Life Balance': f"{work_life}/4",
            'Jarak dari Rumah': f"{dist_home} km",
        }
        st.dataframe(pd.DataFrame(summary.items(), columns=['Atribut','Nilai']),
                     use_container_width=True, hide_index=True)

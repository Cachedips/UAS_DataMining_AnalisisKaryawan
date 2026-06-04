import streamlit as st
import base64, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from assets.style import inject_css

st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")
inject_css()

# Tambahan CSS
st.markdown("""
<style>
.about-member-card {
    background: white;
    border-radius: 20px;
    padding: 28px 24px;
    border: 1px solid rgba(99,179,237,0.25);
    box-shadow: 0 6px 24px rgba(13,31,62,0.09);
    text-align: center;
    transition: all 0.35s ease;
    position: relative;
    overflow: hidden;
}
.about-member-card::before {
    content:'';
    position:absolute; top:0; left:0; right:0;
    height: 5px;
    background: linear-gradient(90deg, #185FA5, #1D9E75);
}
.about-member-card:hover {
    transform: translateY(-6px) scale(1.01);
    box-shadow: 0 20px 50px rgba(13,31,62,0.16);
    border-color: #63b3ed;
}
.about-photo {
    width: 110px; height: 110px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid #185FA5;
    box-shadow: 0 4px 16px rgba(24,95,165,0.3);
    margin: 0 auto 14px;
    display: block;
    transition: all 0.35s ease;
}
.about-member-card:hover .about-photo {
    border-color: #1D9E75;
    transform: scale(1.07);
    box-shadow: 0 8px 28px rgba(29,158,117,0.35);
}
.about-avatar {
    width: 110px; height: 110px;
    border-radius: 50%;
    background: linear-gradient(135deg, #0d1f3e, #185FA5);
    display: flex; align-items: center; justify-content: center;
    font-size: 44px;
    border: 4px solid rgba(99,179,237,0.4);
    box-shadow: 0 4px 16px rgba(24,95,165,0.2);
    margin: 0 auto 14px;
    transition: all 0.35s ease;
}
.about-member-card:hover .about-avatar {
    background: linear-gradient(135deg, #185FA5, #1D9E75);
    transform: scale(1.07);
}
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class='page-header'>
    <h1>ℹ️ About — Informasi Proyek</h1>
    <p>Penjelasan metode, dataset, algoritma, dan tim pengembang</p>
</div>
""", unsafe_allow_html=True)

def img_to_b64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return None

left, right = st.columns([1.1, 0.9], gap="large")

# ═════════════════════════════════
# KIRI
# ═════════════════════════════════
with left:
    # CRISP-DM
    st.markdown("""
    <div class='glass-card'>
        <h3 style='color:#0d1f3e; font-size:19px; font-weight:800; margin:0 0 6px;'>
            🔄 Framework: CRISP-DM
        </h3>
        <p style='font-size:13px; color:#64748b; margin:0 0 16px; line-height:1.6;'>
            CRISP-DM (Cross-Industry Standard Process for Data Mining) adalah metodologi
            standar industri yang terdiri dari 6 fase berulang untuk proyek data mining.
        </p>
    """, unsafe_allow_html=True)

    phases = [
        ("#185FA5", "🎯", "1. Business Understanding",
         "Mendefinisikan tujuan bisnis: memprediksi karyawan yang akan resign dan mengelompokkan profil risiko untuk membantu tim HR mengambil keputusan."),
        ("#1a7fc4", "🔍", "2. Data Understanding",
         "Eksplorasi dataset IBM HR (1.470 record, 35 fitur). Analisis distribusi, korelasi, dan pola attrition berdasarkan departemen, jabatan, dan kepuasan kerja."),
        ("#0891B2", "⚙️", "3. Data Preparation",
         "Label encoding fitur kategorikal, menghapus kolom konstan (EmployeeCount, Over18), penanganan imbalanced data menggunakan SMOTE, dan train-test split 80:20."),
        ("#1D9E75", "🤖", "4. Modeling",
         "Dua model digunakan: XGBoost untuk klasifikasi attrition dan K-Means (k=4) untuk segmentasi karyawan berdasarkan profil risiko dan kepuasan."),
        ("#059669", "📊", "5. Evaluation",
         "XGBoost: Accuracy 92.31%, ROC-AUC 0.9738, F1 0.9234. K-Means: Silhouette Score 0.1102 dengan 4 cluster bermakna."),
        ("#0d1f3e", "🚀", "6. Deployment",
         "Aplikasi web berbasis Streamlit dengan fitur prediksi real-time, visualisasi SHAP, dan dashboard analitik interaktif."),
    ]
    for color, icon, title, desc in phases:
        st.markdown(f"""
        <div class='step-box' style='border-left-color:{color};'>
            <b style='color:{color};'>{icon} {title}</b><br>
            <span style='color:#4b5563;'>{desc}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Algoritma
    st.markdown("""
    <div class='glass-card' style='margin-top:0;'>
        <h3 style='color:#0d1f3e; font-size:19px; font-weight:800; margin:0 0 14px;'>
            🧠 Penjelasan Algoritma
        </h3>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🎯 XGBoost (Extreme Gradient Boosting) — Model 1", expanded=False):
        st.markdown("""
        **XGBoost** adalah algoritma ensemble berbasis decision tree menggunakan teknik *gradient boosting*.
        Setiap pohon baru dibangun untuk memperbaiki kesalahan pohon sebelumnya.

        **Keunggulan:**
        - Sangat akurat untuk data tabular/struktural
        - Tahan terhadap outlier dan missing values
        - Mendukung regularisasi L1/L2 untuk mencegah overfitting
        - Compatible dengan SHAP untuk explainability

        **Hyperparameter:** `n_estimators=200`, `max_depth=6`, `learning_rate=0.1`, `subsample=0.8`

        **Hasil:** Accuracy **92.31%** · F1 **0.9234** · ROC-AUC **0.9738**
        """)

    with st.expander("🔵 K-Means Clustering — Model 2", expanded=False):
        st.markdown("""
        **K-Means** mengelompokkan data ke dalam *k* cluster dengan meminimalkan WCSS (inertia).

        **Proses:**
        1. Inisialisasi k centroid secara acak
        2. Assign setiap data ke centroid terdekat (jarak Euclidean)
        3. Update centroid = mean anggota cluster
        4. Ulangi hingga konvergen

        **Penentuan k:** Elbow Method + Silhouette Score → **k=4 optimal**

        **Cluster:** 🟢 Loyal & Puas · 🟡 Berisiko Sedang · 🔴 Burnout · 🔵 Potensial
        """)

    with st.expander("💡 SHAP — Explainable AI (Bonus +2 ⭐)", expanded=False):
        st.markdown("""
        **SHAP** (SHapley Additive exPlanations) dari game theory menjelaskan kontribusi setiap fitur.

        **Visualisasi:**
        - **Bar Plot** → global feature importance
        - **Beeswarm** → distribusi pengaruh semua fitur
        - **Waterfall** → penjelasan prediksi individual (lokal)
        - **Dependence** → hubungan nilai fitur vs SHAP value

        **Interpretasi:** SHAP > 0 → mendorong **Resign** · SHAP < 0 → mendorong **Tidak Resign**

        **Fitur terpenting:** OverTime · MonthlyIncome · YearsAtCompany
        """)

    with st.expander("⚖️ SMOTE — Penanganan Imbalanced Data", expanded=False):
        st.markdown("""
        Dataset tidak seimbang: hanya **16.1%** resign vs 83.9% tidak resign.

        **SMOTE** membuat data sintetis baru dari kelas minoritas dengan interpolasi antar
        k-NN (bukan sekadar duplikasi), sehingga model tidak bias ke kelas mayoritas.

        **Hasil:** Kedua kelas menjadi seimbang → performa model meningkat signifikan.
        """)

# ═════════════════════════════════
# KANAN
# ═════════════════════════════════
with right:
    # ── TIM PENGEMBANG DENGAN FOTO ────────────────────────────────────────────
    st.markdown("""
    <h3 style='color:#0d1f3e; font-size:19px; font-weight:800; margin-bottom:6px;'>
        👥 Tim Pengembang
    </h3>
       """, unsafe_allow_html=True)

    members = [
        {
            "name" : "Audi Pratiwi Naura",
            "nim"  : "24051214145",
            "role" : "Frontend Developer & Visualisasi",
            "photo": "assets/foto_audi.jpg",
            "color": "#185FA5",
            "badge_bg": "#dbeafe",
            "icon" : "👩‍💻",
        },
        {
            "name" : "Febby Aulia Diva Irdani",
            "nim"  : "24051214157",
            "role" : "Data Analyst & ML Engineer",
            "photo": "assets/foto_febby.jpg",
            "color": "#1D9E75",
            "badge_bg": "#dcfce7",
            "icon" : "👩‍💻",
        },
    ]

    mc1, mc2 = st.columns(2, gap="small")
    for col, m in zip([mc1, mc2], members):
        b64 = img_to_b64(m["photo"])
        if b64:
            photo_html = f"""
            <img src='data:image/jpeg;base64,{b64}' class='about-photo'
                 alt='Foto {m["name"]}'/>"""
        else:
            photo_html = f"<div class='about-avatar'>{m['icon']}</div>"

        col.markdown(f"""
        <div class='about-member-card'>
            {photo_html}
            <div style='font-size:16px; font-weight:800; color:#0d1f3e; margin-bottom:4px;'>
                {m['name']}
            </div>
            <div style='font-size:12px; color:#64748b; margin-bottom:8px;'>
                NIM: {m['nim']}
            </div>
            <div style='background:{m["badge_bg"]}; color:{m["color"]}; font-weight:600;
                        font-size:11px; padding:4px 12px; border-radius:20px;
                        display:inline-block; margin-bottom:10px;'>
                {m['role']}
            </div>
            <div style='font-size:11px; color:#94a3b8;'>
                Universitas Negeri Surabaya<br>
                Sistem Informasi · 2026
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Dataset
    st.markdown("""
    <div class='glass-card'>
        <h3 style='color:#0d1f3e; font-size:18px; font-weight:800; margin:0 0 14px;'>
            🗂️ Informasi Dataset
        </h3>
        <table style='width:100%; border-collapse:collapse; font-size:13px;'>
    """, unsafe_allow_html=True)

    rows = [
        ("Nama",          "IBM HR Analytics Employee Attrition & Performance"),
        ("Sumber",        '<a href="https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset" target="_blank" style="color:#185FA5;">Kaggle</a>'),
        ("Publisher",     "IBM Watson Analytics"),
        ("Jumlah Record", "1.470 baris"),
        ("Jumlah Fitur",  "35 fitur (26 numerik, 9 kategorikal)"),
        ("Target",        "Attrition (Yes / No)"),
        ("Missing Values","<span style='color:#1D9E75; font-weight:700;'>Tidak ada ✅</span>"),
        ("Imbalanced",    "<span style='color:#BA7517;'>Ya — 16.1% (diatasi SMOTE)</span>"),
        ("Lisensi",       "Public / Open"),
    ]
    for i, (label, val) in enumerate(rows):
        bg = "#f8faff" if i % 2 == 0 else "white"
        st.markdown(f"""
        <tr style='background:{bg};'>
            <td style='padding:9px 10px; color:#64748b; width:38%;
                       border-radius:6px 0 0 6px;'>{label}</td>
            <td style='padding:9px 10px; font-weight:600; color:#0d1f3e;
                       border-radius:0 6px 6px 0;'>{val}</td>
        </tr>
        """, unsafe_allow_html=True)

    st.markdown("</table></div>", unsafe_allow_html=True)

    # Teknologi
    st.markdown("""
    <div class='glass-card'>
        <h3 style='color:#0d1f3e; font-size:18px; font-weight:800; margin:0 0 14px;'>
            🛠️ Teknologi
        </h3>
    """, unsafe_allow_html=True)

    techs = ["Python 3.12","Streamlit","XGBoost","Scikit-learn",
             "SHAP","Pandas","NumPy","Plotly","Imbalanced-learn",
             "Matplotlib","Seaborn","Joblib","CRISP-DM","SMOTE"]
    pills = "".join([f"<span class='tech-pill'>{t}</span>" for t in techs])
    st.markdown(f"{pills}</div>", unsafe_allow_html=True)

    # Referensi
    st.markdown("""
    <div class='glass-card'>
        <h3 style='color:#0d1f3e; font-size:18px; font-weight:800; margin:0 0 14px;'>
            📚 Referensi
        </h3>
    """, unsafe_allow_html=True)

    refs = [
        "Chen, T. & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. KDD '16.",
        "Lundberg, S. M. & Lee, S. I. (2017). A Unified Approach to Interpreting Model Predictions. NIPS.",
        "MacQueen, J. (1967). Some Methods for Classification and Analysis of Multivariate Observations.",
        "Chawla, N. et al. (2002). SMOTE: Synthetic Minority Over-sampling Technique. JAIR.",
        "Chapman, P. et al. (2000). CRISP-DM 1.0: Step-by-step data mining guide. SPSS Inc.",
        "IBM HR Analytics Dataset. Kaggle (2017). pavansubhasht/ibm-hr-analytics-attrition-dataset",
    ]
    for i, ref in enumerate(refs, 1):
        st.markdown(f"""
        <div class='ref-item'>
            <b style='color:#185FA5;'>[{i}]</b> {ref}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

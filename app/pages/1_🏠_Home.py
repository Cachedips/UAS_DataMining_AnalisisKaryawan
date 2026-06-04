import streamlit as st
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from assets.style import inject_css
import base64

st.set_page_config(
    page_title="Home — IBM HR Analytics",
    page_icon="🏢",
    layout="wide"
)
inject_css()

# ── Helper: load gambar sebagai base64 ────────────────────────────────────────
def img_to_b64(path):
    """Baca gambar dari disk → base64 string untuk ditampilkan di HTML."""
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return None

# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class='page-header' style='text-align:center; padding:52px 40px;'>
    <div style='font-size:58px; margin-bottom:14px; filter:drop-shadow(0 4px 12px rgba(0,0,0,0.3));'>🏢</div>
    <h1 style='font-size:40px; letter-spacing:-0.5px; margin-bottom:10px;'>
        Prediksi Risiko Attrition Karyawan
    </h1>
    <p style='font-size:17px; max-width:600px; margin:0 auto 22px; opacity:.9; line-height:1.6;'>
        Sistem analisis cerdas berbasis Machine Learning untuk mengidentifikasi
        karyawan yang berpotensi resign dan mengelompokkan profil risiko
        menggunakan pendekatan CRISP-DM.
    </p>
    <div>
        <span class='badge badge-white'>🎯 XGBoost Classification</span>
        <span class='badge badge-white'>🔵 K-Means Clustering</span>
        <span class='badge badge-white'>💡 SHAP Explainable AI</span>
        <span class='badge badge-white'>📋 CRISP-DM</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── STAT CARDS ─────────────────────────────────────────────────────────────────
st.markdown("### 📊 Ringkasan Proyek")
c1, c2, c3, c4 = st.columns(4)
stats = [
    ("1.470", "Total Data Karyawan", "#185FA5"),
    ("35",    "Fitur / Atribut",     "#185FA5"),
    ("92.3%", "Akurasi XGBoost",     "#1D9E75"),
    ("16.1%", "Attrition Rate",      "#E24B4A"),
]
for col, (num, label, color) in zip([c1, c2, c3, c4], stats):
    col.markdown(f"""
    <div class='stat-card'>
        <div class='stat-num' style='color:{color};'>{num}</div>
        <div class='stat-label'>{label}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── KONTEN UTAMA ───────────────────────────────────────────────────────────────
left, right = st.columns([1.1, 0.9], gap="large")

with left:
    # Latar belakang
    st.markdown("""
    <div class='glass-card'>
        <h3 style='color:#0d1f3e; font-size:18px; margin:0 0 14px; font-weight:700;'>
            📌 Latar Belakang
        </h3>
        <div style='font-size:14px; color:#374151; line-height:1.75;'>
            <b style='color:#185FA5;'>Attrition</b> (pengunduran diri karyawan) merupakan tantangan
            besar bagi perusahaan. Biaya menggantikan satu karyawan dapat mencapai
            <b>50–200% dari gaji tahunan</b> mereka, belum termasuk hilangnya pengetahuan
            dan produktivitas tim.<br><br>
            Proyek ini menggunakan dataset <b>IBM HR Analytics</b> dari Kaggle
            dengan <b>1.470 data karyawan dan 35 fitur</b>, untuk membangun sistem yang mampu:
            <ul style='margin-top:10px; padding-left:20px;'>
                <li style='margin-bottom:6px;'>🎯 <b>Memprediksi</b> apakah karyawan akan resign (XGBoost Classification)</li>
                <li style='margin-bottom:6px;'>🔵 <b>Mengelompokkan</b> karyawan berdasarkan profil risiko (K-Means)</li>
                <li>💡 <b>Menjelaskan</b> faktor penyebab utama attrition (SHAP)</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # CRISP-DM Timeline
    st.markdown("""
    <div class='glass-card'>
        <h3 style='color:#0d1f3e; font-size:18px; margin:0 0 18px; font-weight:700;'>
            🔄 Framework CRISP-DM
        </h3>
    """, unsafe_allow_html=True)

    steps = [
        ("#185FA5", "1", "Business Understanding",
         "Mendefinisikan tujuan bisnis & kriteria sukses model"),
        ("#1a7fc4", "2", "Data Understanding",
         "EDA: distribusi, korelasi, visualisasi 35 fitur"),
        ("#0891B2", "3", "Data Preparation",
         "Encoding, SMOTE untuk imbalanced data, train-test split 80:20"),
        ("#1D9E75", "4", "Modeling",
         "XGBoost Classification + K-Means Clustering (k=4)"),
        ("#059669", "5", "Evaluation",
         "Accuracy 92.31% | ROC-AUC 0.9738 | Silhouette 0.1102"),
        ("#0d1f3e", "6", "Deployment",
         "Web app Streamlit dengan prediksi real-time & SHAP dashboard"),
    ]
    for color, num, title, desc in steps:
        st.markdown(f"""
        <div class='timeline-item'>
            <div class='tl-dot' style='background:{color};'>{num}</div>
            <div>
                <p class='tl-title'>{title}</p>
                <p class='tl-desc'>{desc}</p>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

with right:
    # ── MEMBER CARDS DENGAN FOTO ─────────────────────────────────────────────
    st.markdown("""
    <h3 style='color:#0d1f3e; font-size:18px; font-weight:700; margin-bottom:14px;'>
        👤 Identitas Anggota Kelompok
    </h3>
    """, unsafe_allow_html=True)

    members = [
        {
            "name" : "Audi Pratiwi Naura",
            "nim"  : "24051214145",
            "role" : "Frontend Developer & Visualisasi",
            "photo": "assets/foto_audi.jpeg",   
            "color": "#185FA5",
            "icon" : "👩‍💻",
        },
        {
            "name" : "Febby Aulia Diva Irdani",
            "nim"  : "24051214157",
            "role" : "Data Analyst & ML Engineer",
            "photo": "assets/foto_febby.jpeg",  
            "color": "#1D9E75",
            "icon" : "👩‍💻",
        },
    ]

    for m in members:
        b64 = img_to_b64(m["photo"])
        if b64:
            photo_html = f"<img src='data:image/jpeg;base64,{b64}' class='member-photo'/>"
        else:
            photo_html = f"<div class='member-avatar'>{m['icon']}</div>"

        st.markdown(f"""
        <div class='member-card'>
            {photo_html}
            <div style='flex:1;'>
                <div style='font-size:16px; font-weight:700; color:#0d1f3e;'>{m['name']}</div>
                <div style='font-size:13px; color:#64748b; margin:3px 0;'>NIM: {m['nim']}</div>
                <div style='font-size:12px; color:{m['color']}; font-weight:600;
                            background:{"#dbeafe" if m["color"]=="#185FA5" else "#dcfce7"};
                            display:inline-block; padding:2px 10px; border-radius:10px; margin-top:4px;'>
                    {m['role']}
                </div>
                <div style='font-size:11px; color:#94a3b8; margin-top:5px;'>
                    Universitas Negeri Surabaya
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size:11px; color:#94a3b8; text-align:center; margin:8px 0 20px;
                padding:8px; background:#f0f5ff; border-radius:8px;'>
        💡 <i>Taruh foto di <b>app/assets/foto_audi.jpg</b> & <b>app/assets/foto_febby.jpg</b></i>
    </div>
    """, unsafe_allow_html=True)

    # Dataset info
    st.markdown("""
    <div class='glass-card'>
        <h3 style='color:#0d1f3e; font-size:18px; margin:0 0 14px; font-weight:700;'>
            🗂️ Informasi Dataset
        </h3>
        <table style='width:100%; border-collapse:collapse; font-size:13px;'>
            <tr>
                <td style='padding:8px 4px; color:#64748b; width:45%; border-bottom:1px solid #e8f2ff;'>Nama Dataset</td>
                <td style='padding:8px 4px; font-weight:600; color:#0d1f3e; border-bottom:1px solid #e8f2ff;'>IBM HR Analytics</td>
            </tr>
            <tr>
                <td style='padding:8px 4px; color:#64748b; border-bottom:1px solid #e8f2ff;'>Sumber</td>
                <td style='padding:8px 4px; font-weight:600; color:#185FA5; border-bottom:1px solid #e8f2ff;'>Kaggle</td>
            </tr>
            <tr>
                <td style='padding:8px 4px; color:#64748b; border-bottom:1px solid #e8f2ff;'>Jumlah Record</td>
                <td style='padding:8px 4px; font-weight:600; color:#0d1f3e; border-bottom:1px solid #e8f2ff;'>1.470 baris</td>
            </tr>
            <tr>
                <td style='padding:8px 4px; color:#64748b; border-bottom:1px solid #e8f2ff;'>Jumlah Fitur</td>
                <td style='padding:8px 4px; font-weight:600; color:#0d1f3e; border-bottom:1px solid #e8f2ff;'>35 fitur</td>
            </tr>
            <tr>
                <td style='padding:8px 4px; color:#64748b; border-bottom:1px solid #e8f2ff;'>Missing Values</td>
                <td style='padding:8px 4px; font-weight:600; color:#1D9E75; border-bottom:1px solid #e8f2ff;'>Tidak ada ✅</td>
            </tr>
            <tr>
                <td style='padding:8px 4px; color:#64748b; border-bottom:1px solid #e8f2ff;'>Task</td>
                <td style='padding:8px 4px; font-weight:600; color:#0d1f3e; border-bottom:1px solid #e8f2ff;'>Classification + Clustering</td>
            </tr>
            <tr>
                <td style='padding:8px 4px; color:#64748b;'>Algoritma</td>
                <td style='padding:8px 4px; font-weight:600; color:#0d1f3e;'>XGBoost + K-Means</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    # CTA buttons
    st.markdown("### 🚀 Mulai Eksplorasi")
    b1, b2 = st.columns(2)
    with b1:
        if st.button("📊 Lihat Dataset", use_container_width=True):
            st.switch_page("pages/2_📊_Dataset_Overview.py")
    with b2:
        if st.button("🤖 Coba Prediksi", use_container_width=True):
            st.switch_page("pages/3_🚀_Prediction.py")

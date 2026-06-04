# 🏢 UAS Data Mining — IBM HR Analytics Attrition Prediction

**Framework:** CRISP-DM | **Model:** XGBoost Classification + K-Means Clustering

---

## 👥 Anggota Kelompok
| Nama | NIM |
|---|---|
| Audi Pratiwi Naura | 24051214145 |
| Febby Aulia Diva Irdani | 24051214157 |

---

## 📁 Struktur Folder
```
UAS_DataMining/
├── dataset/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── notebook/
│   └── analysis.ipynb
├── model/
│   ├── xgb_model.pkl
│   ├── kmeans_model.pkl
│   ├── scaler.pkl
│   ├── encoders.pkl
│   ├── feature_names.pkl
│   ├── cluster_features.pkl
│   ├── shap_explainer.pkl
│   └── pca.pkl
├── app/
│   ├── app.py
│   └── pages/
│       ├── 1_🏠_Home.py
│       ├── 2_📊_Dataset_Overview.py
│       ├── 3_🤖_Prediction.py
│       ├── 4_📈_Visualization.py
│       └── 5_ℹ️_About.py
├── requirements.txt
└── README.md
```

---

## 🚀 Cara Menjalankan

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Jalankan notebook terlebih dahulu
```bash
cd notebook
jupyter notebook analysis.ipynb
# Jalankan SEMUA cell → pastikan folder model/ terisi file .pkl
```

### 3. Jalankan Streamlit App
```bash
cd app
streamlit run app.py
```

Buka browser di `http://localhost:8501`

---

## 📊 Hasil Model

| Model | Metrik | Nilai |
|---|---|---|
| XGBoost Classification | Accuracy | 92.31% |
| XGBoost Classification | F1-Score | 0.9234 |
| XGBoost Classification | ROC-AUC | 0.9738 |
| XGBoost Classification | CV ROC-AUC (5-fold) | 0.9749 ± 0.0055 |
| K-Means Clustering | Silhouette Score | 0.1102 |
| K-Means Clustering | Jumlah Cluster | 4 |

---

## 🌐 Deployment (Bonus +2)

Deploy ke Streamlit Cloud:
1. Push project ke GitHub
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Pilih repo → set `app/app.py` sebagai main file
4. Klik **Deploy!**

---

## 📦 Dataset
- **Nama:** IBM HR Analytics Employee Attrition & Performance
- **Sumber:** [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **Records:** 1.470 | **Fitur:** 35 | **Missing Values:** 0

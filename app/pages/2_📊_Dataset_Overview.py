import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from assets.style import inject_css

st.set_page_config(page_title="Dataset Overview", page_icon="📊", layout="wide")
inject_css()

st.markdown("""
<div class='page-header'>
    <h1>📊 Dataset Overview</h1>
    <p>IBM HR Analytics Employee Attrition & Performance · 1.470 records · 35 features</p>
</div>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    paths = [
        "dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv",
        "../dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv",
        "WA_Fn-UseC_-HR-Employee-Attrition.csv",
    ]
    for p in paths:
        if os.path.exists(p):
            return pd.read_csv(p)
    return None

df = load_data()
if df is None:
    st.error("⚠️ File dataset tidak ditemukan. Pastikan CSV ada di folder `dataset/`")
    st.stop()

tab1, tab2, tab3, tab4 = st.tabs(["📋 Info Dataset", "🔢 Statistik", "📈 Distribusi", "🔥 Korelasi"])

# ── TAB 1 ──────────────────────────────────────────────────────────────────────
with tab1:
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Data",      f"{len(df):,}")
    c2.metric("Fitur",           f"{df.shape[1]}")
    c3.metric("Karyawan Resign", f"{(df['Attrition']=='Yes').sum()}",
              f"{(df['Attrition']=='Yes').mean()*100:.1f}%")
    c4.metric("Missing Values",  "0 ✅")
    c5.metric("Duplikat",        f"{df.duplicated().sum()}")

    st.markdown("<br>", unsafe_allow_html=True)
    left, right = st.columns([1.4, 0.6], gap="large")

    with left:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("#### 📄 Tampilan Data (10 baris pertama)")

        def highlight_attrition(row):
            if row['Attrition'] == 'Yes':
                return ['background-color:#fff0f0; color:#991b1b;'] * len(row)
            return [''] * len(row)

        st.dataframe(
            df.head(10).style.apply(highlight_attrition, axis=1),
            use_container_width=True, height=280
        )
        st.caption("🔴 Baris merah = karyawan yang resign (Attrition: Yes)")
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("#### 🗂️ Tipe Data")
        num_count = (df.dtypes != 'object').sum()
        cat_count = (df.dtypes == 'object').sum()

        fig_type = px.pie(
            values=[num_count, cat_count],
            names=['Numerik', 'Kategorikal'],
            color_discrete_sequence=['#185FA5', '#1D9E75'],
            hole=0.6
        )
        fig_type.update_traces(textinfo='label+value', textfont_size=13)
        fig_type.update_layout(
            height=230, margin=dict(t=10, b=10, l=10, r=10),
            showlegend=True,
            legend=dict(orientation='h', y=-0.12),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_type, use_container_width=True)

        dtype_df = pd.DataFrame({'Kolom': df.columns, 'Tipe': df.dtypes.astype(str).values})
        st.dataframe(dtype_df, use_container_width=True, height=200)
        st.markdown("</div>", unsafe_allow_html=True)

# ── TAB 2 ──────────────────────────────────────────────────────────────────────
with tab2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("#### 📐 Statistik Deskriptif — Fitur Numerik")
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    stats_df = df[num_cols].describe().T
    stats_df['missing'] = df[num_cols].isnull().sum()
    stats_df = stats_df.round(2)
    stats_df.columns = ['Count','Mean','Std','Min','Q1','Median','Q3','Max','Missing']
    st.dataframe(
        stats_df.style
            .background_gradient(subset=['Mean'], cmap='Blues')
            .background_gradient(subset=['Std'], cmap='YlOrBr')
            .format(precision=2),
        use_container_width=True, height=420
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("#### 📊 Distribusi Fitur Kategorikal vs Attrition Rate")

    cat_cols = df.select_dtypes(include='object').columns.tolist()
    col_sel  = st.selectbox("Pilih fitur kategorikal:", cat_cols,
                             index=cat_cols.index('Department'))

    val_counts = df[col_sel].value_counts().reset_index()
    val_counts.columns = [col_sel, 'Jumlah']
    attr_rate = df.groupby(col_sel)['Attrition'].apply(
        lambda x: (x=='Yes').mean()*100
    ).reset_index()
    attr_rate.columns = [col_sel, 'Attrition Rate (%)']
    val_counts = val_counts.merge(attr_rate, on=col_sel)

    cl, cr = st.columns(2)
    with cl:
        fig_bar = px.bar(val_counts, x=col_sel, y='Jumlah',
                         color='Jumlah', color_continuous_scale='Blues',
                         title=f'Jumlah Karyawan per {col_sel}')
        fig_bar.update_layout(height=350, coloraxis_showscale=False,
                               plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_bar, use_container_width=True)

    with cr:
        avg_rate = df['Attrition'].eq('Yes').mean()*100
        fig_attr = px.bar(val_counts, x=col_sel, y='Attrition Rate (%)',
                          color='Attrition Rate (%)',
                          color_continuous_scale='RdYlGn_r',
                          title=f'Attrition Rate per {col_sel}')
        fig_attr.add_hline(y=avg_rate, line_dash='dash', line_color='navy',
                           annotation_text=f'Rata-rata: {avg_rate:.1f}%',
                           annotation_position='top right')
        fig_attr.update_layout(height=350, coloraxis_showscale=False,
                                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_attr, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── TAB 3 ──────────────────────────────────────────────────────────────────────
with tab3:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("#### 📈 Distribusi Fitur Numerik vs Attrition")

    key_features = ['Age','MonthlyIncome','DistanceFromHome','YearsAtCompany',
                    'TotalWorkingYears','WorkLifeBalance','JobSatisfaction','EnvironmentSatisfaction']
    feat_sel = st.selectbox("Pilih fitur numerik:", key_features, index=0)

    no_data  = df[df['Attrition']=='No'][feat_sel]
    yes_data = df[df['Attrition']=='Yes'][feat_sel]

    cl, cr = st.columns(2)
    with cl:
        fig_hist = go.Figure()
        fig_hist.add_trace(go.Histogram(x=no_data, name='Tidak Resign',
                                        marker_color='#185FA5', opacity=0.72, nbinsx=25))
        fig_hist.add_trace(go.Histogram(x=yes_data, name='Resign',
                                        marker_color='#E24B4A', opacity=0.72, nbinsx=25))
        fig_hist.update_layout(barmode='overlay', height=350,
                               title=f'Histogram: {feat_sel}',
                               plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_hist, use_container_width=True)

    with cr:
        fig_box = go.Figure()
        fig_box.add_trace(go.Box(y=no_data,  name='Tidak Resign',
                                  marker_color='#185FA5', boxmean=True))
        fig_box.add_trace(go.Box(y=yes_data, name='Resign',
                                  marker_color='#E24B4A', boxmean=True))
        fig_box.update_layout(height=350, title=f'Box Plot: {feat_sel}',
                              plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_box, use_container_width=True)

    comp = pd.DataFrame({
        'Statistik'    : ['Mean','Median','Std Dev','Min','Max'],
        'Tidak Resign' : [f"{no_data.mean():.2f}", f"{no_data.median():.2f}",
                          f"{no_data.std():.2f}",  f"{no_data.min():.2f}",  f"{no_data.max():.2f}"],
        'Resign'       : [f"{yes_data.mean():.2f}", f"{yes_data.median():.2f}",
                          f"{yes_data.std():.2f}",  f"{yes_data.min():.2f}",  f"{yes_data.max():.2f}"],
    })
    st.dataframe(comp, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("#### 🔵 Scatter Plot Antar Fitur")
    sc1, sc2 = st.columns(2)
    with sc1:
        x_feat = st.selectbox("Sumbu X:", key_features, index=0, key='sx')
    with sc2:
        y_feat = st.selectbox("Sumbu Y:", key_features, index=1, key='sy')

    fig_sc = px.scatter(df, x=x_feat, y=y_feat, color='Attrition',
                        color_discrete_map={'No':'#185FA5','Yes':'#E24B4A'},
                        opacity=0.55, height=420,
                        title=f'{x_feat} vs {y_feat} — diwarnai berdasarkan Attrition',
                        hover_data=['Department','JobRole','MonthlyIncome'])
    fig_sc.update_layout(legend_title='Attrition',
                         plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    fig_sc.update_xaxes(showgrid=True, gridcolor='#e8f2ff')
    fig_sc.update_yaxes(showgrid=True, gridcolor='#e8f2ff')
    st.plotly_chart(fig_sc, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── TAB 4 ──────────────────────────────────────────────────────────────────────
with tab4:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("#### 🔥 Heatmap Korelasi Fitur Numerik")
    num_df = df.select_dtypes(include=np.number)
    corr   = num_df.corr()

    fig_heat = px.imshow(corr, color_continuous_scale='RdBu_r',
                         zmin=-1, zmax=1, text_auto='.2f', aspect='auto', height=700)
    fig_heat.update_traces(textfont_size=9)
    fig_heat.update_layout(title='Korelasi Pearson antar Fitur Numerik',
                           coloraxis_colorbar_title='r',
                           paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_heat, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("#### 🏆 Top 10 Fitur Berkorelasi Tertinggi")
    target_feat = st.selectbox("Pilih fitur referensi:", num_df.columns.tolist(),
                                index=list(num_df.columns).index('MonthlyIncome'))
    top_corr = corr[target_feat].drop(target_feat).abs().sort_values(ascending=False).head(10)
    fig_top = px.bar(x=top_corr.values, y=top_corr.index, orientation='h',
                     color=top_corr.values, color_continuous_scale='Blues',
                     labels={'x':'|Korelasi|','y':'Fitur'},
                     title=f'Top 10 Fitur Berkorelasi dengan {target_feat}', height=380)
    fig_top.update_layout(coloraxis_showscale=False, yaxis=dict(autorange='reversed'),
                           plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_top, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

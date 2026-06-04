GLOBAL_CSS = """
<style>
/* ═══════════════════════════════════════════
   FONT & BASE
═══════════════════════════════════════════ */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ═══════════════════════════════════════════
   SIDEBAR — Deep Navy Blue
═══════════════════════════════════════════ */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #060d1f 0%, #0d1f3e 40%, #0f2d5e 100%) !important;
    border-right: 1px solid rgba(99,179,237,0.15);
}
[data-testid="stSidebar"] * { color: #c8deff !important; }
[data-testid="stSidebar"] a:hover { color: #63b3ed !important; }

/* Nav links hover */
[data-testid="stSidebarNavLink"] {
    border-radius: 10px !important;
    transition: all 0.25s ease !important;
}
[data-testid="stSidebarNavLink"]:hover {
    background: rgba(99,179,237,0.12) !important;
    transform: translateX(4px);
}
[data-testid="stSidebarNavLink"][aria-current="page"] {
    background: linear-gradient(90deg,rgba(99,179,237,0.25),rgba(29,158,117,0.15)) !important;
    border-left: 3px solid #63b3ed;
}

/* ═══════════════════════════════════════════
   MAIN BACKGROUND
═══════════════════════════════════════════ */
.main .block-container {
    background: #f0f5ff;
    padding-top: 1.5rem !important;
}

/* ═══════════════════════════════════════════
   PAGE HEADER BANNER
═══════════════════════════════════════════ */
.page-header {
    background: linear-gradient(135deg, #0d1f3e 0%, #185FA5 60%, #1a7fc4 100%);
    border-radius: 20px;
    padding: 32px 36px;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 8px 32px rgba(13,31,62,0.35);
    position: relative;
    overflow: hidden;
}
.page-header::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 220px; height: 220px;
    border-radius: 50%;
    background: rgba(255,255,255,0.05);
}
.page-header::after {
    content: '';
    position: absolute;
    bottom: -60px; left: 30%;
    width: 300px; height: 300px;
    border-radius: 50%;
    background: rgba(99,179,237,0.07);
}
.page-header h1 {
    font-size: 28px; font-weight: 800;
    margin: 0 0 6px; letter-spacing: -0.3px;
}
.page-header p { font-size: 14px; opacity: .85; margin: 0; }

/* ═══════════════════════════════════════════
   GLASS CARD — reusable
═══════════════════════════════════════════ */
.glass-card {
    background: rgba(255,255,255,0.92);
    backdrop-filter: blur(10px);
    border-radius: 18px;
    padding: 24px;
    border: 1px solid rgba(99,179,237,0.2);
    box-shadow: 0 4px 20px rgba(13,31,62,0.08);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    margin-bottom: 16px;
}
.glass-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 36px rgba(13,31,62,0.14);
    border-color: rgba(99,179,237,0.45);
}

/* ═══════════════════════════════════════════
   STAT CARD
═══════════════════════════════════════════ */
.stat-card {
    background: white;
    border-radius: 16px;
    padding: 22px 16px;
    text-align: center;
    border: 1px solid rgba(99,179,237,0.2);
    box-shadow: 0 4px 16px rgba(13,31,62,0.07);
    transition: all 0.25s ease;
    cursor: default;
}
.stat-card:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0 16px 40px rgba(13,31,62,0.15);
    border-color: #63b3ed;
}
.stat-num  { font-size: 34px; font-weight: 800; color: #185FA5; line-height: 1; }
.stat-label{ font-size: 12px; color: #64748b; margin-top: 6px; font-weight: 500; }

/* ═══════════════════════════════════════════
   MEMBER CARD (with photo)
═══════════════════════════════════════════ */
.member-card {
    background: white;
    border-radius: 18px;
    padding: 24px;
    border: 1px solid rgba(99,179,237,0.2);
    box-shadow: 0 4px 20px rgba(13,31,62,0.07);
    display: flex;
    align-items: center;
    gap: 18px;
    margin-bottom: 14px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}
.member-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 4px; height: 100%;
    background: linear-gradient(180deg, #185FA5, #1D9E75);
    border-radius: 0 0 0 18px;
}
.member-card:hover {
    transform: translateX(6px);
    box-shadow: 0 12px 36px rgba(13,31,62,0.14);
    border-color: #63b3ed;
}
.member-photo {
    width: 72px; height: 72px;
    border-radius: 50%;
    object-fit: cover !important;
    object-position: center 15% !importants; 
    border: 3px solid #185FA5;
    flex-shrink: 0;
    transition: transform 0.3s ease;
}
.member-card:hover .member-photo { transform: scale(1.08); }
.member-avatar {
    width: 72px; height: 72px; border-radius: 50%;
    background: linear-gradient(135deg,#185FA5,#1D9E75);
    display: flex; align-items: center; justify-content: center;
    font-size: 26px; flex-shrink: 0;
    border: 3px solid rgba(99,179,237,0.3);
    transition: transform 0.3s ease;
}
.member-card:hover .member-avatar { transform: scale(1.08); }

/* ═══════════════════════════════════════════
   BUTTON
═══════════════════════════════════════════ */
div.stButton > button {
    background: linear-gradient(135deg, #0d1f3e 0%, #185FA5 100%);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 28px;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.2px;
    transition: all 0.25s ease;
    box-shadow: 0 4px 14px rgba(24,95,165,0.35);
}
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(24,95,165,0.5);
    background: linear-gradient(135deg, #185FA5 0%, #1a7fc4 100%);
}
div.stButton > button:active { transform: translateY(0px); }

/* ═══════════════════════════════════════════
   METRIC
═══════════════════════════════════════════ */
div[data-testid="metric-container"] {
    background: white;
    border: 1px solid rgba(99,179,237,0.25);
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 2px 12px rgba(13,31,62,0.06);
    transition: all 0.25s ease;
}
div[data-testid="metric-container"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(13,31,62,0.12);
    border-color: #63b3ed;
}

/* ═══════════════════════════════════════════
   TABS
═══════════════════════════════════════════ */
button[data-baseweb="tab"] {
    font-weight: 600 !important;
    border-radius: 10px 10px 0 0 !important;
    transition: all 0.2s ease !important;
}
button[data-baseweb="tab"]:hover {
    background: rgba(99,179,237,0.1) !important;
    color: #185FA5 !important;
}
button[aria-selected="true"][data-baseweb="tab"] {
    color: #185FA5 !important;
    border-bottom: 3px solid #185FA5 !important;
}

/* ═══════════════════════════════════════════
   BADGE / PILL
═══════════════════════════════════════════ */
.badge {
    display: inline-block;
    padding: 5px 16px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    margin: 3px;
    transition: transform 0.2s ease;
}
.badge:hover { transform: scale(1.05); }
.badge-white  { background: rgba(255,255,255,0.18); color: white; border: 1px solid rgba(255,255,255,0.3); }
.badge-blue   { background: #dbeafe; color: #1e40af; }
.badge-green  { background: #dcfce7; color: #166534; }
.badge-amber  { background: #fef3c7; color: #92400e; }
.badge-navy   { background: #1e3a5f; color: #93c5fd; }

/* ═══════════════════════════════════════════
   STEP / TIMELINE
═══════════════════════════════════════════ */
.timeline-item {
    display: flex; gap: 16px; margin-bottom: 14px;
    align-items: flex-start;
    transition: transform 0.2s ease;
}
.timeline-item:hover { transform: translateX(4px); }
.tl-dot {
    width: 38px; height: 38px; border-radius: 50%; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; font-weight: 700; color: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
.tl-title { font-size: 14px; font-weight: 700; color: #0d1f3e; margin: 0 0 3px; }
.tl-desc  { font-size: 12px; color: #64748b; margin: 0; line-height: 1.5; }

/* ═══════════════════════════════════════════
   INFO TABLE ROW HOVER
═══════════════════════════════════════════ */
tr:hover td { background: #f0f7ff !important; transition: background 0.2s; }

/* ═══════════════════════════════════════════
   STEP BOX (About page)
═══════════════════════════════════════════ */
.step-box {
    background: #f8faff;
    border-radius: 12px;
    padding: 14px 18px;
    border-left: 4px solid #185FA5;
    margin-bottom: 10px;
    font-size: 13px;
    color: #374151;
    line-height: 1.6;
    transition: all 0.25s ease;
}
.step-box:hover {
    background: #e8f2ff;
    border-left-color: #1D9E75;
    transform: translateX(4px);
    box-shadow: 0 4px 12px rgba(24,95,165,0.1);
}

/* ═══════════════════════════════════════════
   REF ITEM
═══════════════════════════════════════════ */
.ref-item {
    padding: 10px 16px;
    background: #f8faff;
    border-radius: 10px;
    margin-bottom: 8px;
    font-size: 13px;
    color: #374151;
    border-left: 3px solid #1D9E75;
    transition: all 0.2s ease;
}
.ref-item:hover {
    background: #e6f7f2;
    transform: translateX(4px);
    border-left-color: #185FA5;
}

/* ═══════════════════════════════════════════
   TECH PILL
═══════════════════════════════════════════ */
.tech-pill {
    display: inline-block;
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    margin: 4px;
    background: linear-gradient(135deg, #e0f2fe, #dbeafe);
    color: #0369a1;
    border: 1px solid rgba(99,179,237,0.3);
    transition: all 0.2s ease;
}
.tech-pill:hover {
    transform: translateY(-2px) scale(1.05);
    background: linear-gradient(135deg, #185FA5, #1a7fc4);
    color: white;
    box-shadow: 0 4px 12px rgba(24,95,165,0.3);
}

/* ═══════════════════════════════════════════
   SCROLLBAR
═══════════════════════════════════════════ */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #f0f5ff; }
::-webkit-scrollbar-thumb { background: #93c5fd; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #185FA5; }
</style>
"""

def inject_css():
    import streamlit as st
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

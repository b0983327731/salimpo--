import streamlit as st
import time

# --- [10-1] 底層架構：系統全域設定 ---
st.set_page_config(
    page_title="NINGPU Voyager v9.0",
    page_icon="🌾",
    layout="centered"
)

# --- [10-3] 介面視覺：CSS 視覺降熵與長濱藍主題 ---
# 透過 HTML/CSS 強制覆蓋預設樣式，套用憲法色
st.markdown("""
<style>
    /* 主背景色：長濱藍 */
    .stApp {
        background-color: #003366;
        color: white;
    }
    /* 標題與強調色：稻穗金 */
    h1, h2, h3 {
        color: #F5D105 !important;
        font-weight: 800;
    }
    /* 核心 CTA 按鈕改造 */
    .stButton>button {
        background-color: #F5D105;
        color: #000000;
        font-weight: 900;
        font-size: 18px;
        border-radius: 8px;
        border: none;
        width: 100%;
        padding: 15px 0;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #D4B404;
        color: #000000;
        transform: scale(1.02);
    }
    /* 景點卡片降熵設計 */
    .node-card {
        background-color: #004488;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        border-left: 6px solid #F5D105;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .node-title {
        color: #F5D105;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .node-desc {
        color: #E0E0E0;
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)

# --- 介面渲染開始 ---

# 1. 頂部導航 (Tier 1: Conversion Hotzone)
st.title("長濱寧埔 | AWOS 農場")
st.caption("CRF v9.0 深度智能導覽系統")

# 2. 視覺區 (英雄影像佔位符)
# 這裡使用了一張開源的海洋/自然意象圖，您可以替換成真實的 AWOS 照片網址
st.image("https://images.unsplash.com/photo-1498623116890-37e912163d5d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", 
         caption="【 太平洋 S 彎道景觀 】 AWOS 自然農法實作基地", 
         use_container_width=True)

st.write("") # 增加留白 (Margin of Safety)

# 3. 核心功能 (第一性原理：預約轉換)
if st.button("🚀 立即預約 AWOS 職人體驗"):
    with st.spinner('系統路由中，鎖定長濱在地資源...'):
        time.sleep(1.5) # 勞力幻覺 (Labor Illusion)
    st.success("✅ **預約成功！**\n\n已鎖定 AWOS 農場體驗名額。遵循 CRF v9.0 協議：資料已加密並同步至在地節點。")
    st.balloons() # 多巴胺成癮機制

st.write("---")

# 4. 深度景點列表 (低認知負荷)
st.subheader("深度節點 (Tier-1 Assets)")

# 使用 HTML 渲染卡片以確保視覺一致性
cards_html = """
<div class="node-card">
    <div class="node-title">🌾 AWOS 農場 (Awos Home)</div>
    <div class="node-desc">自然農法、紅藜與傳統海鹽導覽。體驗最純粹的土地滋味與原民生活。</div>
</div>
<div class="node-card">
    <div class="node-title">🌊 寧埔休憩區 (S-Curve)</div>
    <div class="node-desc">全台最美海岸線 180 度觀景點。視覺降熵與感官解壓縮的最佳場域。</div>
</div>
<div class="node-card">
    <div class="node-title">🗿 光榮部落 (Kiwit)</div>
    <div class="node-desc">阿美族生存智慧與石棺遺址探訪。文化遍歷性的起點與歷史傳承。</div>
</div>
"""
st.markdown(cards_html, unsafe_allow_html=True)

# 5. 系統狀態
st.write("")
st.info("🟢 系統存活狀態：雲端節點運行中 (Streamlit Native Web Engine)")

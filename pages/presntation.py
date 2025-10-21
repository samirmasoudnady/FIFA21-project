
import streamlit as st
from time import sleep

# ======= PAGE CONFIG =======
st.set_page_config(
    page_title="FIFA 21 Market Value Prediction",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======= CUSTOM STYLES =======
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: #FFFFFF;
}
h1, h2 {
    color: #F9A825;
    text-align: center;
}
h3 {
    color: #FFB300;
    margin-bottom: 0.4em;
}
.slide-box {
    background-color: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    padding: 2.5rem;
    margin-top: 1.5rem;
    box-shadow: 0px 3px 12px rgba(255, 186, 8, 0.15);
    animation: fadeIn 0.8s ease-in-out;
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}
.list-box {
    background-color: rgba(255, 255, 255, 0.07);
    border-left: 4px solid #FFB300;
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 1rem;
}
.point {
    font-size: 18px;
    line-height: 1.6em;
}
.footer {
    text-align: center;
    color: #BDBDBD;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)


# ======= SLIDES =======
slides = [
    {
        "emoji": "⚽",
        "title": "FIFA 21 Player Market Value Prediction",
        "content": """
        <h3>Project Overview</h3>
        <div class="list-box">
        - Complete analysis of FIFA 21 dataset. <br>
        - Data preprocessing, transformation & cleaning. <br>
        - AI model (CatBoost) for predicting player market value (€). <br>
        - Interactive Streamlit dashboard with insights.
        </div>
        <p style='text-align:center; color:#BBBBBB; font-style:italic;'>Uncover what makes a footballer worth millions! 🧠</p>
        """
    },
    {
        "emoji": "🧹",
        "title": "Data Cleaning Overview",
        "content": """
        <div class="list-box">
        - Removal of unnecessary columns (70+ dropped). <br>
        - Converted height from feet→cm & weight from lbs→kg. <br>
        - Transformed 'value', 'wage', and 'release clause' from € strings to numbers. <br>
        - Dropped missing-heavy columns: <b>'team & contract'</b>, <b>'loan date end'</b>. <br>
        - Cleaned rating columns ('W/F', 'SM', 'IR') → numeric stars (1–5). <br>
        - Applied <b>Log transformation</b> for skewed financial features.
        </div>
        <p style='text-align:center; color:#A5D6A7;'>✅ Clean, consistent, and ready for modeling!</p>
        """
    },
    {
        "emoji": "🧩",
        "title": "Detailed Feature Processing",
        "content": """
        <div class="list-box">
        <h3>Numeric Transformations</h3>
        - Height → <b>height (cm)</b><br>
        - Weight → <b>weight (kg)</b><br>
        - Financials → <b>value, wage, release clause</b> (converted from €, K, M)<br><br>
        <h3>Categorical Transformations</h3>
        - Rating columns → <b>W/F, SM, IR</b> converted to numeric.<br>
        - Removed redundant visuals: <b>player photo, club logo, flag photo</b>.<br><br>
        <h3>Dropped Positional Attributes</h3>
        - Attack, defense & GK role duplicates:<br>
        <i>LS, ST, LW, RW, CAM, CB, GK reflexes...</i><br>
        </div>
        <p style='text-align:center; color:#FFF59D;'>⚙️ Each column prepared with precision for model input.</p>
        """
    },
    {
        "emoji": "📊",
        "title": "EDA Correlation Analysis",
        "content": """
        <div class="list-box">
        - Strong correlation found between <b>total stats</b>, <b>base stats</b>, and <b>market value</b>.<br>
        - Offensive features (dribbling, finishing, short passing) dominate influence.<br>
        - Defensive and GK stats show low predictive power.<br>
        - Age group <b>25–30</b> peaks in market value.<br>
        </div>
        <p style='text-align:center; color:#81D4FA;'>📈 Skill attributes explain player worth better than physique.</p>
        """
    },
    {
        "emoji": "🌍",
        "title": "EDA Insights & Patterns",
        "content": """
        <div class="list-box">
        - Spain 🇪🇸 & Brazil 🇧🇷 lead total market value distribution. <br>
        - Attackers (ST, CAM, RW) dominate top-value clusters. <br>
        - Age vs Value → mid-career players more valuable. <br>
        - Visualization tools: <b>Seaborn, Plotly, Matplotlib</b>.<br>
        </div>
        <p style='text-align:center; color:#FFB74D;'>📊 EDA revealed the story behind football’s economics!</p>
        """
    },
    {
        "emoji": "🤖",
        "title": "Model Development",
        "content": """
        <div class="list-box">
        - Models tested: Linear Regression, Random Forest, CatBoost. <br>
        - <b>CatBoost</b> chosen for superior handling of categorical data. <br>
        - Achieved R² ≈ 0.90 with low RMSE. <br>
        - Combined preprocessing + model pipeline.
        </div>
        <p style='text-align:center; color:#FFD54F;'>🏆 CatBoost takes the trophy home!</p>
        """
    },
    {
        "emoji": "🚀",
        "title": "Key Insights & Future Work",
        "content": """
        <div class="list-box">
        - Skill metrics dominate over physical ones in impact. <br>
        - International reputation consistently adds value. <br>
        - Future work: Add FIFA 22/23 data, use SHAP explainability, deploy cloud app.
        </div>
        <p style='text-align:center; color:#FF7043;'>⚽ Data meets football — and the game becomes smarter!</p>
        """
    }
]

# ======= STATE =======
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

slide = slides[st.session_state.slide_index]

# ======= DISPLAY =======
st.markdown(f"<h1>{slide['emoji']} {slide['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<div class='slide-box'>{slide['content']}</div>", unsafe_allow_html=True)

# ======= NAVIGATION =======
if "slide_index" not in st.session_state:
    st.session_state["slide_index"] = 0

current_slide = st.session_state["slide_index"]

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous", key=f"prev_{current_slide}"):
        st.session_state["slide_index"] = max(0, st.session_state["slide_index"] - 1)
        st.rerun()

with col2:
    st.markdown(
        f"<p style='text-align:center; color:#999;'>Slide {st.session_state.slide_index+1}/{len(slides)}</p>",
        unsafe_allow_html=True)

with col3:
    if st.button("➡️ Next", key=f"next_{current_slide}"):
        st.session_state["slide_index"] = min(len(slides) - 1, st.session_state["slide_index"] + 1)
        st.rerun()

def go_to(page):
    st.session_state["fade"] = True
    sleep(0.3)
    st.session_state["current_page"] = page
    
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    if st.button("⬅️ Back"):
        go_to("pages\modeling.py")
        st.switch_page("pages\modeling.py")

with nav3:
    if st.button("➡️ Next"):
        go_to("home_page.py")
        st.switch_page("home_page.py")

# ======= FOOTER =======
st.markdown("<p class='footer'>📊 FIFA 21 Market Value Analysis — Crafted by Samir Masoud</p>", unsafe_allow_html=True)

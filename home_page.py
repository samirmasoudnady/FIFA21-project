
import sys
import streamlit as st
from time import sleep
sys.path.append('.')   
from custom_transformers import LogTransformer, Handle_outliers_lb_ub, FrequencyEncoder

st.set_page_config(page_title="FIFA 21 Analysis", page_icon="⚽",
                     layout="wide",initial_sidebar_state="collapsed")

st.markdown("""<h1 style="color:white;text-align:center;">  Player Market value of FIFA 21 prediction 📈</h1>""",
             unsafe_allow_html= True)

# dark mode theme
st.markdown("""<style>/* Background & text color */
        body { background-color: #0E1117;color: white;}
        /* Streamlit container tweaks */.stApp 
        {background-color: #0E1117;}
        h1, h2, h3, h4, h5, h6 {color: #FFA500;  
        /* orange accent */font-family: 'Segoe UI', sans-serif;}
        p {color: #E0E0E0;}
        /* Button styling */div.stButton >
        button {background-color: #5353ec;
        color: white; border-radius: 12px;font-weight: bold;}
        div.stButton > button:hover {background-color: #FFA500;
        color: #000;}</style>""", unsafe_allow_html=True)

image_path = "images/7.jpg"
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(image_path, width=700)

st.markdown("""<p style='text-align:center; color:red; font-size:18px;'>Discover insights, analyze data, 
and predict FIFA 21 Player Market Values Using CatBoost Models.</p>""", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4, gap="large")
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

def go_to(page):
    st.session_state["fade"] = True
    sleep(0.3)
    st.session_state["current_page"] = page

with col1:
    if st.button("ℹ️ About"):
        go_to("pages/about.py")
        st.switch_page("pages/about.py")

with col2:
    if st.button("📊 EDA"):
        go_to("pages/eda1.py")
        st.switch_page("pages/eda1.py")

with col3:
    if st.button("🤖 Modeling"):
        go_to("pages/modeling.py")
        st.switch_page("pages/modeling.py")

with col4:
    if st.button("📈 Presentation"):
        go_to("pages/presntation.py")
        st.switch_page("pages/presntation.py")

if "fade" in st.session_state and st.session_state["fade"]:
    st.markdown( """<style>.stApp {animation: fadeEffect 0.7s;}@keyframes fadeEffect {from {opacity: 0;}
            to {opacity: 1;}}</style>""", unsafe_allow_html=True)
    st.session_state["fade"] = False




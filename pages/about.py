
import streamlit as st
from time import sleep
import pandas as pd

df = pd.read_csv('pages/eda_df.csv')
    
# ========== PAGE TITLE ==========
st.markdown(""""<h4 style="color:white;text-align:center;">⚽ Player Market Value Dataset Overview</h4>""", unsafe_allow_html=True)
st.markdown(""" <style> .overview-container { color: orange; font-family: 'Segoe UI', sans-serif;
                text-align: justify;} </style> 
    <div class="overview-container">
        <p>
            The <b>FIFA 21 dataset</b> from <i>Kaggle</i> brings the world of football into data form —
            featuring over <b>18,000 players</b> from clubs and national teams worldwide.
            Each record captures who a player is, how they perform, and what makes them valuable.
        </p>
        <p>
            It combines <b>numerical stats</b> like <i>age, pace, shooting, passing,</i> and
            <i>overall rating</i> with <b>categorical details</b> such as
            <i>nationality, club, position,</i> and <i>preferred foot</i>.
            The star of the show is the <b>market_value</b> — the estimated worth of each player in euros.
        </p>
        <p>
            This dataset goes beyond raw numbers — it tells the story of how
            <b>talent, skill, and reputation</b> translate into market value.
            It’s a dream playground for analysts and data scientists aiming to explore
            what truly makes a player worth millions.
        </p>
    </div> """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ========== BASIC INFO ==========
col1, col2, col3 = st.columns(3)
col1.metric("🧍 Total Players", f"{len(df):,}")
col2.metric("📊 Total Columns", f"{df.shape[1]}")
col3.metric("🌍 Nationalities", f"{df['nationality'].nunique()}")
st.markdown("<hr>", unsafe_allow_html=True)

# ========== COLUMN DESCRIPTIONS ==========
st.markdown("<div class='subheader'>📘 Column Descriptions</div>", unsafe_allow_html=True)

# Data dictionary (column name → description)
data_dict = {
    "name": "The player's full name.",
    "age": "The player’s age in years.",
    "nationality": "The country the player represents.",
    "club": "The football club where the player currently plays.",
    "position": "Detailed position(s) on the field (e.g., CM, RW, CDM).",
    "best_position": "The player’s main or most effective position.",
    "foot": "Preferred foot (Left or Right).",
    "height": "The player’s height in cm.",
    "weight": "The player’s weight (kg or lbs).",
    "over_all_rating": "The player’s overall rating.",
    "best_over_rating": "Best overall rating across all positions.",
    "potential": "Potential future rating (especially for young players).",
    "growth": "Difference between potential and current rating.",
    "intl_reputation": "International reputation (1–5 stars).",
    "total_stats": "Sum of all individual skill attributes.",
    "base_stats": "Core stats excluding advanced or positional ones.",
    "phys_index": "Custom physical ability index.",
    "skill_index": "Custom technical skill index.",
    "pace": "Speed and acceleration combined.",
    "shooting": "Finishing and shot power.",
    "passing": "Passing accuracy and vision.",
    "dribbling": "Ball control and agility.",
    "defense": "Tackling and marking ability.",
    "physical": "Strength, stamina, and jumping.",
    "cross": "Crossing accuracy.",
    "stamina": "Energy and endurance level.",
    "weak_foot": "Skill level with non-dominant foot (1–5).",
    "skill_moves": "Skill moves ability (1–5).",
    "attack_work_rate": "Player’s attacking effort (High/Medium/Low).",
    "defence_work_rate": "Defensive effort (High/Medium/Low).",
    "market_value": "Estimated player market value (€).",
    "contract": "Contract status or years left.",
    "hits": "Popularity or profile views on the platform."
}

# Convert dictionary to DataFrame
dict_df = pd.DataFrame(list(data_dict.items()), columns=["Column Name", "Description"])

# Display in a nice table
st.dataframe(dict_df, use_container_width=True)

# ========== SAMPLE DATA ==========
st.markdown("<div class='subheader'>🧾 Sample Data</div>", unsafe_allow_html=True)
st.dataframe(df, use_container_width=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ========== Categorical COLUMN DESCRIPTIONS ==========
st.markdown("<div class='subheader'>📘 Some info to describe catgorical data</div>", unsafe_allow_html=True)
st.dataframe(df.describe(include= 'object').round(2))

# ========== FOOTER ==========
st.markdown("<br><hr><center style='color:gray;'> Let's go to The Next Stage. </center>", unsafe_allow_html=True)

def go_to(page):
    st.session_state["fade"] = True
    sleep(0.3)
    st.session_state["current_page"] = page

nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    if st.button("⬅️ Back"):
        go_to("home_page.py")
        st.switch_page("home_page.py")

with nav3:
    if st.button("➡️ Next"):
        go_to("pages/eda1.py")
        st.switch_page("pages/eda1.py")

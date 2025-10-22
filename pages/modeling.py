
from streamlit_pandas_profiling import st_profile_report
from sklearn.base import BaseEstimator, TransformerMixin
from ydata_profiling import  ProfileReport
import streamlit as st
from time import sleep
import pandas as pd
import numpy as np
import joblib
import base64
import sys
from custom_transformers import LogTransformer, Handle_outliers_lb_ub, FrequencyEncoder
import types
import __main__

__main__.LogTransformer = LogTransformer
__main__.Handle_outliers_lb_ub = Handle_outliers_lb_ub
__main__.FrequencyEncoder = FrequencyEncoder


# ========== PAGE TITLE ==========
st.markdown(""""<h4 style="color:white;text-align:center;">🧠 Prediction Model</h4>""", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

cl_df = pd.read_csv('pages/cleaned_df.csv')
st.dataframe(cl_df.head(10))
st.markdown("<hr>", unsafe_allow_html=True)  

# --- Input Section ---
st.subheader("⚙️ Input Player Attributes")

nationality = st.selectbox('Nationality', cl_df.nationality.unique())
club = st.selectbox('Club', cl_df.club.unique())
best_position = st.selectbox('Best Position', cl_df.best_position.unique())
foot = st.radio('Foot', ['Right', 'Left'])
attack_work_rate = st.radio('Attack Work Rate', ['Low', 'Medium', 'High'])
defence_work_rate = st.radio('Defence Work Rate', ['Low', 'Medium', 'High'])

height = st.number_input('Height (cm)', step=0.1)
weight = st.number_input('Weight (kg)', step=0.1)
contract = st.number_input('Contract (years)', step=1)
weak_foot = st.number_input('Weak Foot', step=1)
skill_moves = st.number_input('Skill Moves', step=1)
intl_reputation = st.number_input('International Reputation', step=1)

# Sliders for numeric values
age = st.slider('Player Age', int(cl_df.age.min()), int(cl_df.age.max()), step=1)
over_all_rating = st.slider('Overall Rating', int(cl_df.over_all_rating.min()), int(cl_df.over_all_rating.max()), step=1)
potential = st.slider('Potential', int(cl_df.potential.min()), int(cl_df.potential.max()), step=1)
cross = st.slider('Cross', int(cl_df.cross.min()), int(cl_df.cross.max()), step=1)
stamina = st.slider('Stamina', int(cl_df.stamina.min()), int(cl_df.stamina.max()), step=1)
total_stats = st.slider('Total Stats', int(cl_df.total_stats.min()), int(cl_df.total_stats.max()), step=1)
pace = st.slider('Pace', int(cl_df.pace.min()), int(cl_df.pace.max()), step=1)
shooting = st.slider('Shooting', int(cl_df.shooting.min()), int(cl_df.shooting.max()), step=1)
passing = st.slider('Passing', int(cl_df.passing.min()), int(cl_df.passing.max()), step=1)
dribbling = st.slider('Dribbling', int(cl_df.dribbling.min()), int(cl_df.dribbling.max()), step=1)
defense = st.slider('Defense', int(cl_df.defense.min()), int(cl_df.defense.max()), step=1)
physical = st.slider('Physical', int(cl_df.physical.min()), int(cl_df.physical.max()), step=1)
phys_index = st.slider('Physics Index', float(cl_df.phys_index.min()), float(cl_df.phys_index.max()), step=0.1)
skill_index = st.slider('Skill Index', float(cl_df.skill_index.min()), float(cl_df.skill_index.max()), step=0.1)

st.markdown("<hr>", unsafe_allow_html=True)

my_model = joblib.load('pages/Catboost.pkl')
new_data = pd.DataFrame([{
'age': age,
'over_all_rating': over_all_rating,
'nationality': nationality,
'club': club,
'best_position': best_position,
'potential': potential,
'height': height,
'weight': weight,
'foot': foot,
'contract': contract,
'cross': cross,
'stamina': stamina,
'total_stats': total_stats,
'weak_foot': weak_foot,
'skill_moves': skill_moves,
'attack_work_rate': attack_work_rate,
'defence_work_rate': defence_work_rate,
'intl_reputation': intl_reputation,
'pace': pace,
'shooting': shooting,
'passing': passing,
'dribbling': dribbling,
'defense': defense,
'physical': physical,
'phys_index': phys_index,
'skill_index': skill_index }])

predict_button = st.button('Predicted Player Market Value')
if predict_button:
    result = my_model.predict(new_data).round(1)[0]
    st.write(f"💰 Predicted Player Market Value: {result:,.0f} €")

def go_to(page):
    st.session_state["fade"] = True
    sleep(0.3)
    st.session_state["current_page"] = page
    
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    if st.button("⬅️ Back"):
        go_to("pages/eda1.py")
        st.switch_page("pages/eda1.py")

with nav3:
    if st.button("➡️ Next"):
        go_to("pages/presntation.py")
        st.switch_page("pages/presntation.py")



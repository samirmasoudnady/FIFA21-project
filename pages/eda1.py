
import streamlit as st
from ydata_profiling import  ProfileReport
import matplotlib.pyplot as plt
import plotly.express as px 
from time import sleep
import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv('pages/eda_df.csv')

# ========== PAGE TITLE ==========
st.markdown(""""<h4 style="color:white;text-align:center;">📊 Exploratory Data Analysis</h4>""", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ========== BASIC INFO ==========
col1, col2, col3 = st.columns(3)
col1.metric("🧍 Total Numrical Columns", f"{len(df.select_dtypes(include= 'number').columns)}")
col2.metric("📊 Total Categorical Columns", f"{len(df.select_dtypes(include= 'object').columns)}")
col3.metric("🌍 Club", f"{df['club'].nunique()}")

st.markdown("<hr>", unsafe_allow_html=True)

tab_1, tab_2, tab_3 = st.tabs(["📊 Univariate Analysis", "📈 Bivariate Analysis", "📉 Multivariate Analysis"])

with tab_1:
    st.markdown('<style> .center-div {color: red; text-align: center;} </style> <div class="center-div">Univariate Analysis</div>', unsafe_allow_html=True)
    num_cols = df.select_dtypes(include= 'number')
    for col in num_cols.columns:
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
        sns.histplot(df[col], kde=True, ax=axes[0])
        sns.boxplot(x=df[col], ax=axes[1])
        st.pyplot(fig)
        plt.close(fig)

    st.markdown("<hr>", unsafe_allow_html=True)

    stats = ['pace', 'shooting', 'passing',	'dribbling','defense', 'physical']
    for col in stats:
        fig = px.box(df, x='best_position', y=col,
                    title=f'{col.upper()} Distribution by Best_Position',
                    color='best_position')
        st.plotly_chart(fig)

with tab_2:
    st.markdown('<style> .center-div {color: red; text-align: center;} </style> <div class="center-div">Bivariate Analysis</div>', unsafe_allow_html=True)

    report_button = st.button('Show Report')

    if report_button:

        report = ProfileReport(df, title = 'Player Market Value Prediction FIFA21')

        st.write(st_profile_report(report))

with tab_3:
    st.markdown('<style> .center-div {color: red; text-align: center;} </style> <div class="center-div">Multivariate Analysis</div>', unsafe_allow_html=True)
    
    st.markdown("<style> .center-div1 {color: red; text-align: left;} </style> <div class='center-div1'>1.What  is the feature most strongly correlate with target col player market value?</div>", unsafe_allow_html=True)
    strong_corr = df.corr(numeric_only=True).drop('market_value')['market_value'].sort_values(ascending=False)
    fig_1= px.bar(data_frame= strong_corr, x= strong_corr.head(15).index, y= strong_corr.head(15).values, 
    color= strong_corr.head(15).index, title= "Top 15 Features Most Correlated with Player Market Value", 
    labels= {'x':'Feature', 'y':'Correlation Coefficient'})
    fig_1.update_layout(bargap=0.01, bargroupgap=0.05)
    st.plotly_chart(fig_1)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<style> .center-div1 {color: red; text-align: left;} </style> <div class='center-div1'>2.What is the Top 15 Nationality in the Game?</div>", unsafe_allow_html=True)
    nat_count_df = df.groupby('nationality').apply(lambda x:x['name'].count()).reset_index(name='counts')
    nat_count_df.sort_values(by='counts', ascending= False, inplace=True)
    top_15 = nat_count_df[:15]
    fig_2 = px.bar(data_frame= top_15, x='nationality', y='counts', color='counts',
    title = 'the Top 15 Nationality in the FIFA Game', text_auto= True)
    st.plotly_chart(fig_2)  
    st.markdown("<div class='subheader'> note the most player in the game can more 50% from palyers from top seven</div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<style> .center-div1 {color: red; text-align: left;} </style> <div class='center-div1'>3.Which nation has the most number of over performing players?</div>", unsafe_allow_html=True)
    nat_df1 = df.groupby('nationality')['over_all_rating'].mean().reset_index(name='over_all_rating')
    nat_df2 = df.groupby('nationality')['over_all_rating'].count().reset_index(name='player_count')
    merge_df = pd.merge(nat_df1, nat_df2, how='inner',left_on='nationality',right_on='nationality')
    new_df = merge_df[merge_df['player_count'] >= 200].sort_values(by=['over_all_rating','player_count'],ascending=[False,False])
    fig_3 = px.scatter(new_df, x='over_all_rating', y='player_count', color='player_count', size='over_all_rating',
                        hover_data=['nationality'], title='nationality Player counts and Average Potential')
    st.plotly_chart(fig_3)
    st.markdown("<div class='subheader'> note England has produced 1660 players, and still is having an average of 63.56, while Brazil has the highest average Ratings among the players</div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<style> .center-div1 {color: red; text-align: left;} </style> <div class='center-div1'>4.Which Team has the most number of Over Performing Players?</div>", unsafe_allow_html=True)
    club_df1 = df.groupby('club')['over_all_rating'].mean().reset_index(name='over_all_rating')
    club_df2 = df.groupby('club')['over_all_rating'].count().reset_index(name='player_count')
    club_merge_df = pd.merge(club_df1, club_df2, how='inner',left_on='club',right_on='club')
    club_new_df = club_merge_df[club_merge_df['player_count'] >= 25].sort_values(by=['over_all_rating','player_count'],ascending=[False,False])
    fig_4 = px.scatter(club_new_df, x='over_all_rating', y='player_count', color='player_count', size='over_all_rating',
                        hover_data=['club'], title='club Player counts and Average Potential')
    st.plotly_chart(fig_4)
    st.markdown("""<div class='subheader'> note as Bayern_Munich The team which has the highest average rating among all
    the teams (81.24) from a set of 26 players. Another team is Manchester_United which has the highest average among the teams with 45 layers.
    They have an average of 75.866 on the 45 players. Another Team is Real_Madrid has second higest average of 79.28 on the 32 players</div>""", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<style> .center-div1 {color: red; text-align: left;} </style> <div class='center-div1'>5.which postion has the largest number of players?</div>", unsafe_allow_html=True)
    best_df = df.groupby('best_position')['name'].count().reset_index(name='counts')
    best_df.sort_values(by='counts', ascending= False, inplace=True)
    top_15 = best_df[:15]
    fig_5 = px.bar(top_15, x='best_position', y='counts', color='counts', title='Player Postion counts in FIFA 21',
                    labels={'x':'position'}, text_auto= True)
    st.plotly_chart(fig_5)
    st.markdown("""<div class='subheader'> note as the most number of player population is for the Center Back Position,
    which is followed by Striker and The Central attacking midfielder positions in FIFA21 games.</div>""", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<style> .center-div1 {color: red; text-align: left;} </style> <div class='center-div1'>6.Which positions tend to have the highest market values?</div>", unsafe_allow_html=True)
    new_df1 = df.groupby(['best_position', 'foot'])['market_value'].mean().sort_values(ascending= False).reset_index()
    fig_6 = px.bar(data_frame= new_df1, x= 'best_position', y= 'market_value', color= 'foot', barmode='group')
    st.plotly_chart(fig_6)
    st.markdown("""<div class='subheader'> note as the highest player market value for (attacking Postion) in for Right Wing Position,
    which is followed by Striker(centre forward) and The Central attacking midfielder positions in FIFA21 games. </div> """, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<style> .center-div1 {color: red; text-align: left;} </style> <div class='center-div1'>7.Which nationalities produce the most valuable players?</div>", unsafe_allow_html=True)
    new_df2 = df.groupby(['nationality'])['market_value'].sum().sort_values(ascending= False).reset_index()
    fig_7 = px.bar(data_frame= new_df2.head(15), x= 'nationality', y= 'market_value', color= 'nationality', 
    labels={'nationality':'Nationality', 'market_value':'The Most Valuable player '})
    st.plotly_chart(fig_7)
    st.markdown("""<div class='subheader'>note as the player higest market value Spain players, which is followed by Brazil Players.</div>""", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<style> .center-div1 {color: red; text-align: left;} </style> <div class='center-div1'>8.How does player value change with age?</div>", unsafe_allow_html=True)
    fig_8 = px.scatter(data_frame= df, x='age', y='market_value', color='best_position', height= 700, width= 1200)
    new_df5 = df.groupby(['age'])['market_value'].mean().sort_values(ascending= False).reset_index()
    fig_9 = px.bar(data_frame= new_df5, x= 'age', y='market_value', color= 'age')
    st.plotly_chart(fig_8)
    st.plotly_chart(fig_9)
    st.markdown("<div class='subheader'>note the age the primairy key to controll player value and the higest market value almost age from 25 : 30 years old</div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("<style> .center-div1 {color: red; text-align: left;} </style> <div class='center-div1'>9.What’s the relationship of player overall rating and potential ?</div>", unsafe_allow_html=True)
    fig_10 = px.scatter(data_frame= df, x='over_all_rating', y='potential', color='market_value', height= 700, width= 1200)
    st.plotly_chart(fig_10)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<style> .center-div1 {color: red; text-align: left;} </style> <div class='center-div1'>10.Who are the best players in the game?</div>", unsafe_allow_html=True)
    top_play = df[['name', 'over_all_rating', 'age','club','best_position']]
    top_play.sort_values(by='over_all_rating',ascending=False,inplace=True)
    top_100_play = top_play[:100]
    fig_11 = px.scatter(top_100_play, x='age', y='over_all_rating', color='age', size='over_all_rating',
                        hover_data=['name', 'club', 'best_position'], title='Top Football Players in the FIFA 21 game')
    st.plotly_chart(fig_11)
    st.markdown("<div class='subheader'>the 2 top player in fifa 2021 Ronaldo in Juventus & Messi in Barcelona</div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<style> .center-div1 {color: red; text-align: left;} </style> <div class='center-div1'>11.Best Over_all Team in FiFA 2021 </div>", unsafe_allow_html=True)
    final_team = df[['name', 'age', 'over_all_rating','best_position','club']]
    final_team.sort_values(by='age',inplace=True)
    pos_play = final_team.groupby('best_position')['over_all_rating'].max().reset_index(name='Overall Score')
    player_pos = pd.merge(final_team, pos_play, how='inner', left_on=['best_position','over_all_rating'], 
                            right_on=['best_position','Overall Score'])
    pos_best = player_pos[['name', 'club', 'age', 'best_position', 'Overall Score']]
    st.dataframe(pos_best)
    st.image('images/players1.png')
    st.markdown("<hr>", unsafe_allow_html=True)


    st.markdown("<style> .center-div1 {color: red; text-align: left;} </style> <div class='center-div1'>12.the Best Team with the players with the highest potential </div>", unsafe_allow_html=True)
    pot_team = df[['name', 'age', 'potential','best_position','club']]
    pot_team.sort_values(by='age',inplace=True)
    pos_df = pot_team.groupby('best_position')['potential'].max().reset_index(name='potential')
    new_pot_df = pd.merge(pot_team, pos_df, how='inner', left_on=['best_position','potential'], 
                        right_on=['best_position','potential'])
    pot_df = new_pot_df[['name', 'club', 'age', 'best_position', 'potential']]
    cm = sns.light_palette("black", as_cmap=True)
    pot_df[0:15].style.background_gradient(cmap=cm)
    st.dataframe(pot_df[0:15])
    st.image('images/players.png')
    st.markdown("<hr>", unsafe_allow_html=True)

def go_to(page):
    st.session_state["fade"] = True
    sleep(0.3)
    st.session_state["current_page"] = page
    
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    if st.button("⬅️ Back"):
        go_to("pages/about.py")
        st.switch_page("pages/about.py")

with nav3:
    if st.button("➡️ Next"):
        go_to("pages\modeling.py")
        st.switch_page("pages\modeling.py")

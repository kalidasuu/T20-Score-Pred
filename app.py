import streamlit as st
import pickle
import pandas as pd
import numpy as np


pipe = pickle.load(open('pipe.pkl','rb'))

# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFFuo4V4q-m4Y3RC7UaN_vpsjdSagFW04WUQ&s");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


input_style = """
<style>
input[type="text"] {
    background-color: transparent;
    color: #a19eae;  // This changes the text color inside the input box
}
div[data-baseweb="base-input"] {
    background-color: transparent !important;
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;
}
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)

teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka',
         'Nepal',
         'Netherlands',
         'Ireland']

cities = ['Florida','Adelaide', 'Al Amerat', 'Hobart', 'Brisbane', 'Dubai', 'Kolkata', 'Delhi', 'Geelong', 'Dharamsala', 'Bangalore', 'Melbourne', 'Perth', 'Mohali', 'Sharjah', 'Dhaka', 'Sydney', 'Sylhet', 'Jamtha', 'Mumbai', 'Chattogram', 'Abu Dhabi']

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(works for over>5)')
with col5:
    wickets = st.number_input('Wickets out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs

    input_df = pd.DataFrame(
     {'batting_team': batting_team, 'bowling_team': bowling_team,'current_score': current_score,'wickets_left': wickets_left,'balls_left': balls_left,'last_five': last_five,'crr': crr,'city':city},index=[0])
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))



import streamlit as st
import streamlit.components.v1 as components

# Makes the dashboard fill the whole screen width
st.set_page_config(layout="wide")

st.title("NYC Airbnb Dashboard")

# Replace the URL below with your actual Tableau Share Link
# Make sure it has ?:embed=yes at the end!
tableau_url = "https://public.tableau.com/views/project_17756312871780/Dashboard1?:embed=yes&:showVizHome=no"

components.iframe(tableau_url, height=800, scrolling=True)

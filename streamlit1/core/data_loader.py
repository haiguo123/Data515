import streamlit as st
from streamlit1.core.game_logic import load_data

@st.cache_data
def get_game_data():
    return load_data("data/game_data.pkl")
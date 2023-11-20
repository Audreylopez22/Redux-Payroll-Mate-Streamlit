import streamlit as st
import datetime

def log_message(message):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    st.text(f"[{formatted_time}] {message}")
    
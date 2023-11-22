import streamlit as st


st.set_page_config(page_title="Warning and alerts", page_icon="⚠",layout="wide")

st.markdown("#  Warnings and alerts")
st.sidebar.header("Warnings and alerts")

if 'errors' in st.session_state:
    for error in st.session_state.errors:
        st.error(error)

if 'alerts' in st.session_state:
    for alert in st.session_state.alerts:
        st.warning(alert)
        
if 'info' in st.session_state:
    for info in st.session_state.info:
        st.info(info)



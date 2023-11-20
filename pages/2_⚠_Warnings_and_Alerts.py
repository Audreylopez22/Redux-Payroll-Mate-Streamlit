import streamlit as st


st.set_page_config(page_title="Warning and alerts", page_icon="⚠")

st.markdown("#  Warnings and alerts")
st.sidebar.header("Warnings and alerts")


if 'alerts' in st.session_state:
    for alert in st.session_state.alerts:
        st.warning(alert)


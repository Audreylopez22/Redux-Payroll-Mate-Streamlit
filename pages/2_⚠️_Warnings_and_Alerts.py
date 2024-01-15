import streamlit as st

st.set_page_config(page_title="Warning and alerts", page_icon="⚠",layout="wide")

if 'authentication_status' not in st.session_state or st.session_state.authentication_status is None or st.session_state.authentication_status is False:
    st.warning("You must login to access this page.") 
    st.markdown(f'<meta http-equiv="refresh" content="0;url={st.secrets.urls.login}">', unsafe_allow_html=True)
    st.stop() 
    

st.markdown("#  Warnings and alerts")
st.sidebar.header("Warnings and alerts")

if not any(key in st.session_state for key in ['errors', 'alerts', 'info']):
    st.warning("No data loaded. Please upload an Excel file on the load page.")
else:
    
    if 'errors' in st.session_state:
        for error in st.session_state.errors:
            st.error(error)

    if 'alerts' in st.session_state:
        for alert in st.session_state.alerts:
            st.warning(alert)

    if 'info' in st.session_state:
        for info in st.session_state.info:
            st.info(info)



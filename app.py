

import streamlit as st
from pages import home, load_sheet, warnings_and_alerts, country_payroll, documentation
from rules import rules_load_sheet

rules_load_sheet.setup()


page_options = ["Home", "1_📈_Load_Sheet", "2_⚠_Warnings_and_Alerts", "3_🌍_Country_Payroll", "4_📃_Documentation"]
selected_page = st.sidebar.selectbox("Select a page", page_options)


if selected_page == "Home":
    home.show()
elif selected_page == "1_📈_Load_Sheet":
    load_sheet.show()
elif selected_page == "2_⚠_Warnings_and_Alerts":
    warnings_and_alerts.show()
elif selected_page == "3_🌍_Country_Payroll":
    country_payroll.show()
elif selected_page == "4_📃_Documentation":
    documentation.show()

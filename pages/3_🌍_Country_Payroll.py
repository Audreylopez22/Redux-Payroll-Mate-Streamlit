import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Country Payroll", page_icon="🌍",layout="wide")

st.markdown("# Country Payroll")
st.sidebar.header("Country Payroll")


if 'data' not in st.session_state:
    st.session_state.data = None


if st.session_state.data is None:
    st.warning("No data loaded. Please upload an Excel file on the load page.")
else:
    columns = st.session_state.data[0]
    employee_data = st.session_state.data[1:]
    df = pd.DataFrame(employee_data, columns=columns)

    # Count the number of employees by country
    employee_count_by_country = df['Country'].value_counts().reset_index()
    employee_count_by_country.columns = ['Country', 'Employee Count']

    if not employee_count_by_country.empty:
        # Create the choropleth map
        fig = px.choropleth(
            employee_count_by_country,
            locations='Country',
            locationmode='country names',
            color='Employee Count',
            color_continuous_scale='Viridis',
            title='Number of Employees by Country in America',
            labels={'Employee Count': 'Number of Employees'}
        ) 
        fig_bar = px.bar(employee_count_by_country, x='Country', y='Employee Count', title='Number of Employees by Country')

        # Show the chart in Streamlit
        st.plotly_chart(fig)
        st.plotly_chart(fig_bar)
    else:
        st.warning("No data available to display.")
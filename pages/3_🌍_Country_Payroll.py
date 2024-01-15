import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Country Payroll", page_icon="🌍",layout="wide")

# Verificar si la cookie "nomina_key" está presente
if 'authentication_status' not in st.session_state or st.session_state.authentication_status is None or st.session_state.authentication_status is False:
    st.warning("You must login to access this page.")
    st.markdown(f'<meta http-equiv="refresh" content="0;url={st.secrets.urls.login}">', unsafe_allow_html=True)
    st.stop() 

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
        
        fig.update_geos(projection_type="natural earth", showcoastlines=True)
        fig.update_layout(height=800)
        
        fig_bar = px.bar(employee_count_by_country, x='Country', y='Employee Count', title='Number of Employees by Country')
        fig_bar.update_layout(height=500)
        # Show the chart in Streamlit
        st.plotly_chart(fig_bar,use_container_width=True)
        st.plotly_chart(fig ,use_container_width=True)
        
    else:
        st.warning("No data available to display.")
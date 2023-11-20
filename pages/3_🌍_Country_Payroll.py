import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Country Payroll", page_icon="🌍")

st.markdown("# Country Payroll")
st.sidebar.header("Country Payroll")


data = st.session_state.data

columns = data[0]
employee_data = data[1:]
df = pd.DataFrame(employee_data, columns=columns)

# Contar el número de empleados por país
employee_count_by_country = df['Country'].value_counts().reset_index()
employee_count_by_country.columns = ['Country', 'Employee Count']

# Crear el gráfico de mapa
fig =  px.choropleth(
    employee_count_by_country,
    locations='Country',
    locationmode='country names',
    color='Employee Count',
    color_continuous_scale='Viridis',
    title='Número de Empleados por País en América',
    labels={'Employee Count': 'Número de Empleados'}
) 
fig_bar = px.bar(employee_count_by_country, x='Country', y='Employee Count', title='Número de Empleados por País')

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)
st.plotly_chart(fig_bar)
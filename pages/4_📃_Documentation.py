import streamlit as st
import streamlit as st
import openpyxl 
from io import BytesIO
import datetime
import os
import importlib


st.set_page_config(page_title="Documentation", page_icon="📄")

st.markdown("# Documentation")
st.sidebar.header("Documentation")

def main():
    st.header("Introduction")
    st.write("The Excel file processing application is a tool designed to streamline the manipulation of data contained in Excel files. It utilizes Streamlit for the user interface and Openpyxl for data processing.")

    st.header("Streamlit")
    st.write("Streamlit is an open-source framework that makes it easy to create web applications for data analysis and interactive prototypes. With Streamlit, developers can effortlessly turn Python scripts into web applications.")

    st.subheader("Key Features of Streamlit")
    st.write("1. **Simplicity:** With just a few Python commands, it's possible to create interactive interfaces without the need for web development expertise.")
    st.write("2. **Dynamic Updates:** Interface elements automatically update when data or parameters change.")
    st.write("3. **Easy Integration:** Easily integrates with popular libraries such as Pandas, Plotly, and Matplotlib for data visualization.")

    st.header("Openpyxl")
    st.write("Openpyxl is a Python library that allows reading and writing Excel files in xlsx format. With Openpyxl, it's possible to programmatically manipulate spreadsheets, cells, and data.")

    st.subheader("Key Features of Openpyxl")
    st.write("1. **Read and Write:** Enables reading and writing of data in Excel files.")
    st.write("2. **Spreadsheet Manipulation:** Facilitates the creation, duplication, and deletion of spreadsheets.")
    st.write("3. **Cell Formatting:** Allows formatting cells, such as styles, colors, and formulas.")

    st.header("Operation of the Application")
    st.subheader("User Interface with Streamlit:")
    st.write("The user interface is created using Streamlit, providing buttons, progress bars, and alerts for an interactive experience.")

    st.subheader("Data Processing with Openpyxl:")
    st.write("Uploaded Excel files are processed using Openpyxl to apply specific rules defined in the 'rules' folder.")

    st.subheader("Results Visualization:")
    st.write("Interactive charts with Plotly Express are used to display the distribution of employees by country.")


if __name__ == "__main__":
    main()

import streamlit as st

st.set_page_config(page_title="Home", page_icon="👋", layout="wide")

if (
    "authentication_status" not in st.session_state
    or st.session_state.authentication_status is None
    or st.session_state.authentication_status is False
):
    st.warning("You must login to access this page.")
    st.markdown(
        f'<meta http-equiv="refresh" content="0;url={st.secrets.urls.login}">',
        unsafe_allow_html=True,
    )
    st.stop()


def main():
    st.title("Welcome to the Payroll File Processing Tool")

    # Introduction
    st.header("Introduction")
    st.write(
        "The Excel file processing application is a tool designed to streamline the"
        + " manipulation of data contained in Excel files. It utilizes Streamlit for the user"
        + " interface and Openpyxl for data processing."
    )

    # Streamlit
    st.header("Streamlit")
    st.write(
        "Streamlit is an open-source framework that makes it easy to create web applications"
        + " for data analysis and interactive prototypes. With Streamlit, developers can"
        + " effortlessly turn Python scripts into web applications."
    )
    st.subheader("Key Features of Streamlit")
    st.write(
        "1. **Simplicity:** With just a few Python commands, it's possible to create"
        + " interactive interfaces without the need for web development expertise."
    )
    st.write(
        "2. **Dynamic Updates:** Interface elements automatically update when data or"
        + " parameters change."
    )
    st.write(
        "3. **Easy Integration:** Easily integrates with popular libraries such as Pandas,"
        + " Plotly, and Matplotlib for data visualization."
    )

    # Openpyxl
    st.header("Openpyxl")
    st.write(
        "Openpyxl is a Python library that allows reading and writing Excel files in xlsx"
        + " format. With Openpyxl, it's possible to programmatically manipulate spreadsheets,"
        + " cells, and data."
    )
    st.subheader("Key Features of Openpyxl")
    st.write("1. **Read and Write:** Enables reading and writing of data in Excel files.")
    st.write(
        "2. **Spreadsheet Manipulation:** Facilitates the creation, duplication, and deletion"
        + " of spreadsheets."
    )
    st.write(
        "3. **Cell Formatting:** Allows formatting cells, such as styles, colors, and formulas."
    )

    # Operation of the Application
    st.header("Operation of the Application")

    # Page 1: Load an Excel File
    st.header("Page 1: Load an Excel File")
    st.write(
        "1. On the '1_📈_Load_Sheet' page, use the 'Browse Files' button to upload your Excel"
        + " file. Make sure it's in 'xlsx' or 'xls' format and does not exceed 200 MB."
    )
    st.write(
        "2. After uploading the file, the application will automatically check if it contains"
        + " the necessary data. A warning will be shown if the file is empty, and a log message"
        + " will be recorded."
    )
    st.write(
        "3. If the file has valid data, the application will apply modifications based on"
        + " rules defined in the 'rules' folder."
    )
    st.write(
        "4. On the interface, you'll see a progress bar indicating the application's"
        + " progress through the rules. It will check for the presence of two sheets,"
        + " 'Comp Management' and 'Bonus Sheet,' and console messages will display the"
        + " execution of these rules."
    )
    st.write("5. After applying all the rules, a modified file will be generated.")
    st.write(
        "6. You'll see a 'Download Modified File' button. Click to download the modified"
        + " file to your device."
    )

    # Page 2: Warnings and Alerts
    st.header("Page 2: Warnings and Alerts")
    st.write(
        "Here you'll find alerts generated during the execution of the rules. It will display"
        + "individuals celebrating birthdays this month, those completing one year with the company,"
        + "and potential employees with empty cells or missing elements in the data sheet."
    )

    # Page 3: Country Payroll
    st.header("Page 3: Country Payroll")
    st.write("This page features two graphs representing the number of employees per country.")

    # Results Visualization
    st.subheader("Results Visualization:")
    st.write(
        "Interactive charts with Plotly Express are used to display the distribution of"
        + " employees by country."
    )

    # System Requirements
    st.header("System Requirements")
    st.write("1. Python 3.x")
    st.write("2. Libraries: Streamlit, Openpyxl, Pandas, Plotly Express")


if __name__ == "__main__":
    main()

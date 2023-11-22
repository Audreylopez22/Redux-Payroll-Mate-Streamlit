import streamlit as st


st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide"
)


def main():
    st.title("Welcome to the Payroll File Processing Tool")
    st.write("In this application, you'll find a tool designed to streamline the processing of" +
            " payroll files. Follow the steps below to make use of this tool:")

    # Page 1: Load an Excel File
    st.header("Page 1: Load an Excel File")
    st.write("1. On the '1_📈_Load_Sheet' page, use the 'Browse Files' button to upload your Excel"+
            " file. Make sure it's in 'xlsx' or 'xls' format and does not exceed 200 MB.")
    st.write("2. After uploading the file, the application will automatically check if it contains"+
            " the necessary data. A warning will be shown if the file is empty, and a log message" + 
            " will be recorded.")
    st.write("3. If the file has valid data, the application will apply modifications based on"+
            " rules defined in the 'rules' folder.")
    st.write("4. On the interface, you'll see a progress bar indicating the application's"+
            " progress through the rules. It will check for the presence of two sheets,"+
            " 'Comp Management' and 'Bonus Sheet,' and console messages will display the"+
            " execution of these rules.")
    st.write("5. After applying all the rules, a modified file will be generated.")
    st.write("6. You'll see a 'Download Modified File' button. Click to download the modified"+
            " file to your device.")

    # Page 2: Warnings and Alerts
    st.header("Page 2: Warnings and Alerts")
    st.write("Here you'll find alerts generated during the execution of the rules. It will display individuals celebrating birthdays this month, those completing one year with the company, and potential employees with empty cells or missing elements in the data sheet.")

    # Page 3: Country Payroll
    st.header("Page 3: Country Payroll")
    st.write("This page features two graphs representing the number of employees per country.")

    # Page 4: Documentation
    st.header("Page 4: Documentation")
    st.write("Find detailed information about the technologies and methodologies used to build"+
            "  this application.")

if __name__ == "__main__":
    main()

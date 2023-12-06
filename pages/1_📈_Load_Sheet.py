import streamlit as st
import openpyxl 
from io import BytesIO
import datetime
import os
import importlib
import formulas
from tempfile import NamedTemporaryFile

st.set_page_config(page_title="Load Sheet", page_icon="📈",layout="wide")

st.markdown("# Welcome to the Excel file processing application!")
st.sidebar.header("Welcome to the Excel file processing application! ")
st.write(
    """Here, you can upload your Excel file to perform various operations. Start by selecting your 
    file via the 'Load an Excel file' button. The application will automatically check whether the 
    file contains the necessary data. If it does, modifications will be made for the payroll 
    validation process."""
)

def load_data_from_excel(uploaded_file):
    workbook = openpyxl.load_workbook(uploaded_file)
    sheet = workbook.active
    
    data = [[cell.value for cell in row] for row in sheet.iter_rows()]
    return data

def log_message(message):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    st.text(f"[{formatted_time}] {message}")
    
def process_rules(workbook, progress_bar):
    rule_files = [filename for filename in os.listdir('rules') 
                if filename.endswith(".py") and filename not in ["__init__.py"]]
    total_steps = len(rule_files)
    sorted_files =  sorted(rule_files)
    
    for i, filename in enumerate(sorted_files):
        if filename.endswith(".py") and filename not in ["__init__.py"]:
            rule_module_name = f"rules.{filename[:-3]}"
            rule = importlib.import_module(rule_module_name)
            if hasattr(rule, 'main') and callable(rule.main):
                workbook = rule.main(workbook,progress_bar)
        
        #For the progres bar
        progress_percentage = min(1.0, (i + 1) / total_steps)
        progress_bar.progress(progress_percentage)

    return workbook


def main():

    uploaded_file = st.file_uploader("Load an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        
        #to reset the session state when analizyded new information
        st.session_state.alerts = []
        st.session_state.errors = []
        st.session_state.info = []
        st.session_state.logs = []
        st.session_state.tmp_file=[]
        uploaded_file_contents = uploaded_file.read()
        
        if 'file_hash' not in st.session_state or st.session_state.file_hash != hash(uploaded_file_contents):
            st.session_state.file_hash = hash(uploaded_file_contents)
        
        st.session_state.data = load_data_from_excel(uploaded_file)
    
        workbook = openpyxl.load_workbook(uploaded_file)
        sheet = workbook.active

        if sheet.max_row == 1 and sheet.max_column == 1 and sheet.cell(row=1, column=1).value is None:
            st.warning("The Excel file is empty.")
            log_message("The Excel file is empty.")
            
        else:

            progress_bar = st.progress(0.0)
            log_message("Making modifications to the Excel file...")
                
            workbook = process_rules(workbook, progress_bar)
            
            
            # the modified or processed file is saved in memory
            modified_file = BytesIO()
            log_message("Saving modifications to the Excel file...")
            workbook.save(modified_file)
            
            #to display the data in the guarapo tab it is necessary to physically save the 
            # calculated data and it is saved in the files folder. 
            with NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp_file:
                st.session_state.tmp_file = tmp_file.name
                workbook.save(tmp_file.name)
            
            xl_model = formulas.ExcelModel().loads(tmp_file.name).finish()
            xl_model.calculate()
            xl_model.write(dirpath='tmp')
            
            # download button for the downloaded file that is in memory
            st.session_state.download_button = st.download_button(
                label="Download modified file",
                data=modified_file.getvalue(),
                key='download_file.xlsx',
                file_name='modified_file.xlsx',)

if __name__ == "__main__":
    main()
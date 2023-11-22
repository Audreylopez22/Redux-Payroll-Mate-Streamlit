
from tools import log_message
import streamlit as st

def new_employee_alert(sheet):
    log_message(f"checking for new employees this month for sheet: {sheet.title}")

    if sheet.title != "Comp Management":
        return

    # Obtener la columna de status
    status_column_index = None
    header_row = sheet[1]
    for idx, cell in enumerate(header_row, start=1):
        if cell.value == "Status":
            status_column_index = idx
            break

    if  status_column_index is None:
        st.error("No 'Status' column found.")
        return

    # Obtener una lista de personas que se encuentran inavtivas
    status_inactive = "Inactive"
    status_people = []
    
    for row in sheet.iter_rows(min_row=2, max_col=status_column_index, values_only=True):
        status_column = row[status_column_index - 1]
        if isinstance(status_column, str) and status_column.lower() == status_inactive.lower():
            status_people.append(row[0]) 

    if status_people:
        formatted_list = "\n".join([f"- {person}" for person in status_people])
        st.session_state.alerts.append(f"Inactive employees in sheet '{sheet.title}': \n{formatted_list}")

    else:
        st.session_state.info.append(f"No inactive employees were found in the current month.")
            
def main(workbook,progress_bar):
    for sheet in workbook:
        new_employee_alert(sheet)
    if progress_bar is not None:
        progress_bar.progress(1.0 / len(sheet.parent.sheetnames))

    return workbook

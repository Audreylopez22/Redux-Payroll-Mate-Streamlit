
from tools import log_message
import datetime
import streamlit as st

def check_aniversary_alert(sheet):
    log_message(f"Checking aniversary alert for sheet: {sheet.title}")

    if sheet.title != "Comp Management":
        return

    # Obtener la columna de fechas de nacimiento
    hire_date_column_index = None
    header_row = sheet[1]
    for idx, cell in enumerate(header_row, start=1):
        if cell.value == "Hire Date":
            hire_date_column_index = idx
            break

    if hire_date_column_index is None:
        st.error("No 'Hire Date' column found.")
        return

    # Obtener una lista de personas que cumplen años en el mes actual
    today = datetime.date.today()
    hireDate_people = []
    for row in sheet.iter_rows(min_row=2, max_col=hire_date_column_index, values_only=True):
        hire_date = row[hire_date_column_index - 1]
        if isinstance(hire_date, datetime.date) and hire_date.month == today.month:
            hireDate_people.append(row[0]) 

    if hireDate_people:
        formatted_list = "\n".join([f"- {person}" for person in hireDate_people])
        st.session_state.info.append(f"People with an aniversary in the current month in sheet '{sheet.title}' : \n{formatted_list}")

    else:
        st.warning(f"No aniversary in the current month'.")
            
def main(workbook,progress_bar):
    for sheet in workbook:
        check_aniversary_alert(sheet)
    if progress_bar is not None:
        progress_bar.progress(1.0 / len(sheet.parent.sheetnames))

    return workbook

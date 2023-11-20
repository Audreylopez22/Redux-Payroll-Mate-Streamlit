
from tools import log_message
import datetime
import streamlit as st

def check_birthday_alert(sheet):
    log_message(f"Checking birthday alert for sheet: {sheet.title}")

    if sheet.title != "Comp Management":
        return

    # Obtener la columna de fechas de nacimiento
    birth_date_column_index = None
    header_row = sheet[1]
    for idx, cell in enumerate(header_row, start=1):
        if cell.value == "Birth Date":
            birth_date_column_index = idx
            break

    if birth_date_column_index is None:
        st.error("No 'Birth Date' column found.")
        return

    # Obtener una lista de personas que cumplen años en el mes actual
    today = datetime.date.today()
    birthday_people = []
    for row in sheet.iter_rows(min_row=2, max_col=birth_date_column_index, values_only=True):
        birth_date = row[birth_date_column_index - 1]
        if isinstance(birth_date, datetime.date) and birth_date.month == today.month:
            birthday_people.append(row[1]) 

    if birthday_people:
        formatted_list = "\n".join([f"- {person}" for person in birthday_people])
        st.session_state.alerts.append(f"People with birthdays in the current month in sheet '{sheet.title}' : \n{formatted_list}")

    else:
        st.warning(f"No birthdays in the current month'.")
            
def main(workbook,progress_bar):
    for sheet in workbook:
        check_birthday_alert(sheet)
    if progress_bar is not None:
        progress_bar.progress(1.0 / len(sheet.parent.sheetnames))

    return workbook

from tools import log_message
import streamlit as st 

def empty_cells(sheet):
    log_message(f"Checking empty cells for sheet: {sheet.title}")
    
    max_row = sheet.max_row
    max_col = 11
    
    empty_first_column_row = None
    for row in range(1, max_row + 1):
        if sheet.cell(row=row, column=1).value is None:
            empty_first_column_row = row
            break

    if empty_first_column_row is not None:
        max_row = empty_first_column_row - 1
        
    columns = [sheet.cell(row=1, column=col).value for col in range(1, max_col + 1)]
    empty_cells = {}

    for col in range(1, max_col + 1):
        actual_column = columns[col - 1]
        empty_cells_persons = []
        
        for row in range(1, max_row + 1):
            if sheet.title == "Bonus Sheet" and sheet.cell(row=row, column=col).value is None:
                empty_cells_persons.append(sheet.cell(row=row, column=1).value)
            elif sheet.cell(row=row, column=col).value is None:
                empty_cells_persons.append(sheet.cell(row=row, column=2).value)
        
        if empty_cells_persons:
            empty_cells[actual_column] = empty_cells_persons

    if empty_cells:
        formatted_list = "\n".join([f"- Column {col}, people without information: {' ; '.join(persons)}" for col, persons in empty_cells.items()])
        st.session_state.alerts.append(f"Empty cells in sheet '{sheet.title}': \n{formatted_list}")
        
    else:
        log_message(f"No empty cells found in sheet '{sheet.title}'.")

def main(workbook,progress_bar):
    for sheet in workbook:
        empty_cells(sheet)
    if progress_bar is not None:
        progress_bar.progress(1.0 / len(sheet.parent.sheetnames))

    return workbook

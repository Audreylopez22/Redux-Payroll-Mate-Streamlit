from tools import log_message

def process_magnament(sheet):
    if sheet.title == "Comp Management":
        last_row= sheet.max_row
        
        
        for row in range (2, last_row +1):
            # for calculate Non cash out benefits
            could_guru = sheet.cell(row=row, column=sheet['R'][0].column).value or 0 
            accounting_advice = sheet.cell(row=row, column=sheet['T'][0].column).value or 0
            
            sheet.cell(row=row, column=sheet['U'][0].column).value = could_guru  + accounting_advice 
            
            # Designated Cash out benefits 
            p_healt_care = sheet.cell(row=row, column=sheet['O'][0].column).value or 0 
            software_reimbursement = sheet.cell(row=row, column=sheet['P'][0].column).value or 0
            
            sheet.cell(row=row, column=sheet['V'][0].column).value = p_healt_care  + software_reimbursement
            
        return sheet
    
    return sheet

def main(workbook, progress_bar):
    for sheet in workbook:
        process_magnament(sheet)
    
    if progress_bar is not None:
        progress_bar.progress(1.0 / len(sheet.parent.sheetnames))   

    return workbook

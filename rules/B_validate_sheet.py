from tools import log_message

def validate_sheet(sheet):
    log_message(f"Validating sheet: {sheet.title}")

    sheet_configurations = {
        "Comp Management": {"expected_columns": ["Last name, First name", "Country",
                                                "Status","Division","Job Title","Location",
                                                "Paid per","Pay rate","Hire Date","Birth Date",
                                                "Private Health Care Cloud Team Status",
                                                "Private Health Care Cloud Team Company pays",
                                                "Private Health Care Managed Teams Status",
                                                "Private Health Care Managed Teams Company pays",
                                                "Reimbursement for software license Company pays",
                                                "A Cloud Guru 2023 Effective date",
                                                "A Cloud Guru 2023 Company pays", 
                                                "Accounting Advise Status",
                                                "Accounting Advise Company pays"]},
        "Bonus Sheet": {"expected_columns": ["Last name, First name", "City", "Country","Hire Date",
                                            "Birth Date", "Employment Status","Pay rate", 
                                            "Job Title", "Location","Bonus: Date", "Bonus: Amount",
                                            "Bonus: Reason", "Bonus: Comment"]},
    }

    sheet_name = sheet.title

    if sheet_name not in sheet_configurations:
        log_message(f"Sheet '{sheet_name}' is not configured for validation.")
        return False

    expected_columns = sheet_configurations[sheet_name]["expected_columns"]

    header_row = sheet[1]
    column_names = [cell.value for cell in header_row]

    if column_names != expected_columns:
        log_message(f"The columns in sheet '{sheet_name}' are not in the expected order.")
        log_message(f"Expected columns: {expected_columns}")
        log_message(f"Actual columns: {column_names}")
        return False

    log_message(f"The sheet '{sheet_name}' is valid.")
    
    return True

def main(workbook, progress_bar):
    for sheet in workbook:
        validate_sheet(sheet)
    if progress_bar is not None:
        progress_bar.progress(1.0 / len(sheet.parent.sheetnames))

    return workbook
from tools import log_message


def main(workbook, progress_bar):
    expected_sheets = {"Comp Management", "Bonus Sheet"}
    existing_sheets = set(sheet.title for sheet in workbook)

    if expected_sheets.issubset(existing_sheets) and len(existing_sheets) == 2:
        log_message("The document has the required sheets: 'Comp Management' and 'Bonus Sheet'.")

        if progress_bar is not None:
            progress_bar.progress(1.0 / len(workbook.sheetnames))

    else:
        log_message("The document does not have the required sheets")

    return workbook

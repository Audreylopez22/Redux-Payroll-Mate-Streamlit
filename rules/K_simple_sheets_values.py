from tools import log_message


def simple_sheet_values(workbook):
    # Select Sheets
    if "Simple Sheet" in workbook.sheetnames:
        log_message("processing simple sheet")
        comp_management_sheet = workbook["Comp Management"]
        simple_sheet = workbook["Simple Sheet"]

        simple_sheet_dic = {}

        for row in range(2, comp_management_sheet.max_row + 1):
            name = comp_management_sheet.cell(row=row, column=1).value
            base_salary = comp_management_sheet.cell(row=row, column=8).value
            on_going_reimbursements = f"=VLOOKUP(A{row},'Comp Management'!$A$2:$AA${comp_management_sheet.max_row},23,FALSE)"
            sub_total = f"=VLOOKUP(A{row},'Comp Management'!$A$2:$AA${comp_management_sheet.max_row},24,FALSE)"
            comments = f"=VLOOKUP(A{row},'Comp Management'!$A$2:$AA${comp_management_sheet.max_row},25,FALSE)"
            bonus = comp_management_sheet.cell(row=row, column=26).value
            total = comp_management_sheet.cell(row=row, column=27).value

            simple_sheet_dic[name] = [
                base_salary,
                on_going_reimbursements,
                sub_total,
                comments,
                bonus,
                total,
            ]

        simple_sheet.delete_rows(2, simple_sheet.max_row)
        for name, values in simple_sheet_dic.items():
            simple_sheet.append([name] + values)

    return workbook


def main(workbook, progress_bar):
    simple_sheet_values(workbook)

    if progress_bar is not None:
        progress_bar.progress(1.0)

    return workbook

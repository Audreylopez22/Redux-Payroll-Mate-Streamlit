from tools import log_message, get_or_create_money_style


def assign_distributing_payroll(workbook):
    log_message("Assigning distributing payroll from 'Distributing payroll' to 'Simple Sheet'")
    money_style = get_or_create_money_style(workbook)

    if "Distributing payroll" in workbook.sheetnames:
        distributing_payroll_sheet = workbook["Distributing payroll"]
        simple_sheet = workbook["Simple Sheet"]

        distributing_payroll_dict = {}

        for row in range(2, distributing_payroll_sheet.max_row + 1):
            name = distributing_payroll_sheet.cell(row=row, column=1).value
            divided_payroll = distributing_payroll_sheet.cell(row=row, column=2).value
            principal_account = distributing_payroll_sheet.cell(row=row, column=3).value
            principal_account_value = distributing_payroll_sheet.cell(row=row, column=4).value
            secondary_account = distributing_payroll_sheet.cell(row=row, column=5).value

            if divided_payroll:  # Esto asegura que solo se agrega si divided_payroll es True
                distributing_payroll_dict[name] = {
                    "divided_payroll": divided_payroll,
                    "principal_account": principal_account,
                    "principal_account_value": principal_account_value,
                    "secondary_account": secondary_account,
                }

        for row in range(2, simple_sheet.max_row + 1):
            name_in_simple_sheet = simple_sheet.cell(row=row, column=1).value

            if name_in_simple_sheet in distributing_payroll_dict:
                payroll_info = distributing_payroll_dict[name_in_simple_sheet]
                simple_sheet.cell(
                    row=row, column=8, value=payroll_info["divided_payroll"]
                ).style = money_style
                simple_sheet.cell(
                    row=row, column=9, value=payroll_info["principal_account"]
                ).style = money_style
                simple_sheet.cell(
                    row=row, column=10, value=payroll_info["principal_account_value"]
                ).style = money_style
                simple_sheet.cell(
                    row=row, column=12, value=payroll_info["secondary_account"]
                ).style = money_style

    return workbook


def main(workbook, progress_bar):
    assign_distributing_payroll(workbook)

    if progress_bar is not None:
        progress_bar.progress(1.0)

    return workbook

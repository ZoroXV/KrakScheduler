import xlsxwriter as xw

def build_schedule():
    wb = xw.Workbook('schedule.xlsx')
    global_sheet = wb.add_worksheet('Global')
    individual_sheet = wb.add_worksheet('Individual')

    wb.close()

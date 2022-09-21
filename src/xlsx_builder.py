import xlsxwriter as xw

def build_schedule(time_slots, workers, stands):
    wb = xw.Workbook('schedule.xlsx')
    global_sheet = wb.add_worksheet('Global')
    individual_sheet = wb.add_worksheet('Individual')

    build_global_sheet_skeleton(global_sheet, time_slots, stands)

    build_individual_sheet_skeleton(individual_sheet, time_slots, workers)

    wb.close()

def build_global_sheet_skeleton(sheet, time_slots, stands):
    row = 1
    col = 1

    for time_slot in time_slots:
        sheet.write(row, 0, time_slot)
        row += 1

    for stand in stands:
        sheet.write(0, col, stand)
        col += 1

def build_individual_sheet_skeleton(sheet, time_slots, workers):
    row = 1
    col = 1

    for time_slot in time_slots:
        sheet.write(0, col, time_slot)
        col += 1

    for worker in workers:
        sheet.write(row, 0, worker)
        row += 1

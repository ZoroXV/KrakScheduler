import xlsxwriter
from .global_sheet import build_sheet as build_global_sheet
from .individual_sheet import build_sheet as build_individual_sheet

def build_schedule(scheduler):
    wb = xlsxwriter.Workbook('schedule.xlsx')
    global_sheet = wb.add_worksheet('Global')
    individual_sheet = wb.add_worksheet('Individual')
    time_worked_sheet = wb.add_worksheet('Worked Time')

    global_sheet.set_column(0,scheduler.get_event().get_hours_duration(), 30)
    individual_sheet.set_column(0,scheduler.get_event().get_hours_duration(), 15)
    time_worked_sheet.set_column(0,1,15)

    cell_format = wb.add_format({'bold': True, 'font_color': 'red', 'align': 'center'})

    build_global_sheet(global_sheet, scheduler.get_event(), cell_format)
    build_individual_sheet(individual_sheet, scheduler.get_event(), cell_format)
    build_time_worked_sheet(time_worked_sheet, scheduler.get_event())

    return (wb, global_sheet, individual_sheet)

def build_time_worked_sheet(sheet, event):
    sheet.write(0, 0, 'Name')
    sheet.write(0, 1, 'Hours Worked')

    row = 1

    data = []
    for worker in event.get_workers_list():
        data.append((worker.get_name(), worker.get_time_worked()))
    data.sort(key=lambda tup: tup[1])

    for name, time_worked in data:
        sheet.write(row, 0, name)
        sheet.write(row, 1, time_worked)
        row += 1

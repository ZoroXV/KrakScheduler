from asyncio import current_task
import xlsxwriter
from datetime import datetime
from datetime import timedelta

def build_schedule(scheduler):
    wb = xlsxwriter.Workbook('schedule.xlsx')
    global_sheet = wb.add_worksheet('Global')
    individual_sheet = wb.add_worksheet('Individual')

    global_sheet.set_column(0,scheduler.get_event().get_hours_duration(), 30)
    cell_format = wb.add_format({'bold': True, 'font_color': 'red', 'align': 'center'})

    build_stands_names(global_sheet, scheduler.get_event().get_stands_list(), cell_format)
    build_hours_slots(global_sheet, scheduler.get_event())
    build_workers_shifts(global_sheet, scheduler.get_stands_list())

    return (wb, global_sheet, individual_sheet)

def build_stands_names(sheet, stands_list, cell_format):
    row = 0
    col = 1

    for stand in stands_list:
        sheet.write(row, col, stand.get_name(), cell_format)
        col += 1

def build_hours_slots(sheet, event):
    row = 1
    col = 0
    time_format = '%H:%M'

    start_current_shift = event.get_start_hour()

    duration = event.get_hours_duration()
    for i in range (duration):
        end_current_shift = start_current_shift + timedelta(hours = 1)
        sheet.write(row, col, start_current_shift.strftime(time_format) + " - " + end_current_shift.strftime(time_format))
        row += 1
        start_current_shift = end_current_shift

def build_workers_shifts(sheet, stands_list):
    col = 1
    for stand in stands_list:
        row = 1
        for i in range (len(stand.get_staff_needed())):
            workers = stand.get_specific_shift_worker_list(i)
            final_string = ""
            for worker in workers:
                final_string += worker.get_name() + '\n'
            sheet.write(row, col, final_string)
            row += 1
        col += 1

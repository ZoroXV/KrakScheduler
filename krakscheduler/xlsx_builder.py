from asyncio import current_task
from decimal import ROUND_DOWN
import xlsxwriter
from datetime import datetime
from datetime import timedelta

def build_schedule(scheduler):
    wb = xlsxwriter.Workbook('schedule.xlsx')
    global_sheet = wb.add_worksheet('Global')
    individual_sheet = wb.add_worksheet('Individual')

    # set the width of the columns
    global_sheet.set_column(0,scheduler.get_event().get_event_hours_duration(), 30)

    #build_global_sheet_skeleton(global_sheet, time_slots, stands)
    #build_individual_sheet_skeleton(individual_sheet, time_slots, workers)

    # to set the format of a cell
    cell_format = wb.add_format({'bold': True, 'font_color': 'red', 'align': 'center'})

    build_stands_names(global_sheet, scheduler.get_event().get_stands_list(), cell_format)
    build_hours_slots(global_sheet, scheduler.get_event())
    build_workers_shifts(global_sheet, scheduler.get_stands_list())

    return (wb, global_sheet, individual_sheet)

def build_global_sheet_skeleton(sheet, time_slots, stands):
    row = 1
    col = 1

    for time_slot in time_slots:
        sheet.write(row, 0, time_slot)
        row += 1

    for stand, _ in stands:
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

def fill_global_sheet(sheet, duration, schedule):
    row = 1
    col = 1

    for stand in schedule:
        workers = '\n'.join(schedule[stand])
        for slot in range(0, duration):
            sheet.write(row, col, workers)
            col += 1
        col = 1
        row += 1

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

    duration = event.get_event_hours_duration()
    print(duration)
    print(type(duration))
    for i in range (duration):
        end_current_shift = start_current_shift + timedelta(hours = 1)
        sheet.write(row, col, start_current_shift.strftime(time_format) + " - " + end_current_shift.strftime(time_format))
        row += 1
        start_current_shift = end_current_shift

def build_workers_shifts(sheet, stands_list):
    row = 1
    col = 1
    for stand in stands_list:
        row = 1
        for i in range (len(stand.get_staff_needed())):
            workers = stand.get_specific_shift_worker_list(i)
            final_string = ""
            for worker in workers:
                final_string += worker.get_name() + " "
            sheet.write(row, col, final_string)
            row += 1
    col += 1
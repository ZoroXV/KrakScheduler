from datetime import datetime
from datetime import timedelta

def build_sheet(sheet, event, cell_format):
    build_workers_names(sheet, event.get_workers_list())
    build_hours_slots(sheet, event, cell_format)

    row = 1
    for worker in event.get_workers_list():
        build_workers_shifts(sheet, worker, row)
        row += 1

def build_workers_names(sheet, workers):
    row = 1

    for worker in workers:
        sheet.write(row, 0, worker.get_name())
        row += 1

def build_hours_slots(sheet, event, cell_format):
    col = 1
    time_format = '%H:%M'

    start_current_shift = event.get_start_hour()

    duration = event.get_hours_duration()
    for i in range (duration):
        end_current_shift = start_current_shift + timedelta(hours = 1)
        sheet.write(0, col, start_current_shift.strftime(time_format) + " - " + end_current_shift.strftime(time_format), cell_format)
        col += 1
        start_current_shift = end_current_shift

def build_workers_shifts(sheet, worker, row):
    schedule = worker.get_staff_shifts()

    col = 1
    for slot in schedule:
        string = ''
        if slot:
            string = slot.get_name()
        sheet.write(row, col, string)
        col += 1

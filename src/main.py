from xlsx_builder import *
from scheduler.scheduler import Scheduler

def main():
    time_slots = [
            '23h-00h',
            '00h-01h',
            '01h-02h',
            '02h-03h'
        ]

    workers = [
            'worker 1',
            'worker 2',
            'worker 3',
            'worker 4'
        ]

    stands = [
            ['Entrée', 4],
            ['Bar', 6],
            ['Toilettes', 2],
            ['Vestiaire', 3]
        ]

    wb, global_sheet, _ = build_schedule(time_slots, workers, stands)

    scheduler = Scheduler(workers, stands, time_slots)
    scheduler.fill_schedule()

    schedule = scheduler.get_schedule()
    print(schedule)
    fill_global_sheet(global_sheet, len(time_slots), schedule)

    wb.close()

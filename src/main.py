from xlsx_builder import *

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
            'Bar',
            'Entrée',
            'Toilettes',
            'Vestiaire'
        ]

    build_schedule(time_slots, workers, stands)

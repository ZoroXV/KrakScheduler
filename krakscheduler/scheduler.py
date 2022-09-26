import random

class Scheduler:
    schedule = {}

    def __init__(self, event):
        # Event object
        self.event = event
        # Stand object list
        self.stands_list = event.get_stands_list()
        # Worker object list
        self.workers_list = event.get_workers_list()

    def fill_schedule(self):
        workers = self.get_workers_list()
        for stand in self.get_stands_list():
            # Shifts
            for i in range(len(stand.get_staff_needed())):
                while(stand.get_free_places(i) > 0):
                    current_worker = random.choice(workers)
                    while self.is_worker_currently_working(current_worker, i) != 0:
                        current_worker = random.choice(workers)
                    stand.add_worker(current_worker, i)

    def get_schedule(self):
        return self.schedule

    def get_event(self):
        return self.event

    def get_stands_list(self):
        return self.stands_list

    def get_workers_list(self):
        return self.workers_list

    # return the number of places left for the specific stand at a specific shift
    def get_current_shift_remaining_places(self, shift_index, stand):
        return stand.get_free_places(shift_index)

    # return the number of places taken for the specific stand at a specific shift
    def get_current_shift_taken_places(self, shift_index, stand):
        return stand.get_taken_places(shift_index)

    # return the list of current workers at a specific stand and at a specific shift
    def get_current_shift_worker_list(self, shift_index, stand):
        return stand.get_specific_shift_worker_list(shift_index)

    #def create_stands_columns(self, nb_stands, stands_lists)

    # check if the staff is already taken for a shift at a specific time or not
    def is_worker_currently_working(self, worker, shift_index):
        return worker.is_currently_staffing(shift_index)

    # maximum hours of staff that a worker can do
    def staff_already_worked_too_much(self, worker):
        return worker.get_time_worked() >= 4

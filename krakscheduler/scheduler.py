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

    def get_workers_for_stand(self, stand, duration):
        name, quantity = stand
        quantity = quantity if quantity <= len(self.workers) else len(self.workers)

        current_workers = random.sample(self.workers, quantity)
        self.schedule[name] = current_workers

    def fill_schedule(self):
        for stand in self.stands:
            self.get_workers_for_stand(stand, len(self.time_slots))

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
    def is_staff_available(self, worker, shift_index):
        return worker.is_currently_staffing(self, shift_index)

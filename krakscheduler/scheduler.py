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
                    while current_worker.is_working(i) != 0:
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

import random

class Scheduler:
    schedule = {}

    def __init__(self, event):
        self.event = event

    def get_schedule(self):
        return self.schedule

    def get_event(self):
        return self.event

    def fill_schedule(self):
        workers = self.event.get_workers_list()
        for stand in self.event.get_stands_list():
            for i in range(len(stand.get_staff_needed())):
                while(stand.get_free_places(i) > 0):
                    current_worker = random.choice(workers)
                    while current_worker.is_working(i) != 0:
                        current_worker = random.choice(workers)
                    stand.add_worker(current_worker, i)

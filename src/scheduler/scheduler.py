import random

class Scheduler:
    schedule = {}

    def __init__(self, workers, stands, time_slots):
        self.workers = workers
        self.stands = stands
        self.time_slots = time_slots

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

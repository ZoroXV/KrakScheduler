import random

class Scheduler:
    schedule = {}

    def __init__(self, workers, stands):
        self.workers = workers
        self.stands = stands

    def get_workers_for_stand(self, stand):
        name, quantity = stand
        quantity = quantity if quantity <= len(self.workers) else len(self.workers)

        current_workers = random.sample(self.workers, quantity)
        self.schedule[name] = current_workers

    def fill_schedule(self):
        for stand in self.stands:
            self.get_workers_for_stand(stand)

    def get_schedule(self):
        return self.schedule

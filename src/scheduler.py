import random
from event import Event

class Scheduler:
    schedule = {}

    def __init__(self, event):
        self.event = event
        self.stands_list = event.get_stands_list()
        self.staffs_list = event.get_staffs_list()
        # list that will hold x histogram of taken staff for every hour
        # for an event of 7 hour it will hold 7 histogram for example
        self.taken_staffs = self.init_taken_staffs()

    def init_taken_staffs(self):
        taken_staffs = []
        for i in range(self.event.get_event_hours_duration()):
            taken_staffs.append([0]* len(self.staffs_list))
        return taken_staffs
    
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

    #def create_stands_columns(self, nb_stands, stands_lists)

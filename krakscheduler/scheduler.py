import random

class Scheduler:
    def __init__(self, event):
        self.event = event

    def get_schedule(self):
        return self.schedule

    def get_event(self):
        return self.event

    def display(self):
        print('{:=^64}'.format('Schedule Result'))
        for stand in self.event.get_stands_list():
            print('{:=^64}'.format(stand.get_name()))
            for slot in stand.get_worker_list():
                display_list = []
                for worker in slot:
                    display_list.append(worker.get_name())
                print(display_list)

    def fill_schedule(self):
        workers = self.event.get_workers_list()
        for stand in self.event.get_stands_list():
            self.fill_manager(stand)
            for i in range(len(stand.get_staff_needed())):
                while(stand.get_free_places(i) > 0):
                    current_worker = random.choice(workers)
                    while current_worker.is_working(i) != 0 or current_worker.is_manager():
                        current_worker = random.choice(workers)
                    stand.add_worker(current_worker, i)

    def fill_manager(self, stand):
        managers = self.event.get_managers()
        if stand.is_manager_need():
            manager = self.event.pick_random_free_manager()
            stand.add_worker_all(manager)

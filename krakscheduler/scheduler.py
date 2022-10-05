import random

class Scheduler:
    def __init__(self, event):
        self.event = event

    def get_schedule(self):
        return self.schedule

    def get_event(self):
        return self.event

    def display_global(self):
        print('{:=^64}'.format('Schedule Result'))
        for stand in self.event.get_stands_list():
            print('{:=^64}'.format(stand.get_name()))
            for slot in stand.get_worker_list():
                display_list = []
                for worker in slot:
                    display_list.append(worker.get_name())
                print(display_list)

    def display_individual(self):
        print('{:=^64}'.format('Schedule Result'))
        for worker in self.event.get_workers_list():
            print('{:=^64}'.format(worker.get_name()))
            for shift in worker.get_staff_shifts():
                if shift:
                    print(shift.get_name())
                else:
                    print('Break')

    def fill_schedule(self):
        self.fill_managers()

        for stand in self.event.get_stands_list():
            for i in range(len(stand.get_staff_needed())):
                current_free_workers = self.event.get_available_workers(i)
                while(stand.get_free_places(i) > 0):
                    current_worker = random.choice(current_free_workers)
                    stand.add_worker(current_worker, i)

    def fill_managers(self):
        for stand in self.event.get_stands_list():
            self.fill_manager(stand)

    def fill_manager(self, stand):
        if stand.is_manager_need():
            manager = self.event.pick_random_free_manager()
            stand.add_worker_all(manager)

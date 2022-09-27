from datetime import datetime

class Event:
    def __init__(self, name, start_hour, end_hour, stands_list=[], workers_list=[]):
        self.name = name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.stands_list = stands_list
        self.workers_list = workers_list

    def get_name(self):
        return self.name

    def get_nb_stands(self):
        return len(self.stands_list)

    def get_nb_workers(self):
        return len(self.workers_list)

    def get_start_hour(self):
        return self.start_hour

    def get_end_hour(self):
        return self.end_hour

    def get_seconds_duration(self):
        return (self.end_hour - self.start_hour).seconds

    def get_hours_duration(self):
        return int(self.get_seconds_duration() / 3600)

    def get_stands_list(self):
        return self.stands_list

    def get_workers_list(self):
        return self.workers_list

    def add_stand(self, stand):
        self.stands_list.append(stand)

    def remove_stand(self, stand):
        self.stands_list.remove(stand)

    def add_worker(self, worker):
        self.workers_list.append(worker)

    def remove_worker(self, worker):
        self.workers_list.remove(worker)

    def get_managers(self):
        managers = []
        for worker in self.workers_list:
            if worker.is_manager():
                managers.append(worker)
        return managers

    def get_stands_with_manager(self):
        stands = []
        for stand in self.stands_list:
            if stand.is_manager_need():
                stands.append(stand)
        return stands

    def display(self):
        print('{:=^64}'.format(self.name))
        print('{}{:.>54}'.format('Begins at:', datetime.strftime(self.start_hour, '%d/%m/%Y %Hh%M')))
        print('{}{:.>56}'.format('Ends at:', datetime.strftime(self.end_hour, '%d/%m/%Y %Hh%M')))
        print('{:=^64}'.format(''))

        print('{:=^64}'.format('Stands'))
        for stand in self.stands_list:
            stand.display()

        print('{:=^64}'.format('Workers'))
        for worker in self.workers_list:
            worker.display()

        print('{:=^64}'.format('Event End'))

    def pick_random_free_manager(self):
        managers = self.get_managers()
        for manager in managers:
            if manager.get_time_worked() == 0:
                return manager

        return None

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

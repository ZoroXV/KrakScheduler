class Stand:

    def __init__(self, name, staff_needed, shift_duration=1, need_manager=False):
        self.name = name
        self.free_places = staff_needed
        self.taken_places = [0] * len(staff_needed)
        self.staff_needed = staff_needed
        self.shift_duration = shift_duration

        # list that will hold x list containing the names of the staff
        # x will be the length of the event
        self.worker_list = self.init_worker_list()
        self.need_manager = need_manager

    def init_worker_list(self):
        worker_list = []
        for i in range(len(self.staff_needed)):
            worker_list.append([])
        return worker_list

    # get name of the stand
    def get_name(self):
        return self.name

    # get the number of places available in the stand
    def get_places(self, shift_index):
        return self.free_places[shift_index] + self.taken_places[shift_index]

    # get the number of places that still are free
    def get_free_places(self, shift_index):
        return self.free_places[shift_index]

    # get the number of places already taken
    def get_taken_places(self, shift_index):
        return self.taken_places[shift_index]

    def get_shift_duration(self):
        return self.shift_duration

    # get the list of all shifts list
    def get_worker_list(self):
        return self.worker_list

    # get the list of the staffs at a specific shift
    def get_specific_shift_worker_list(self, shift_index):
        return self.worker_list[shift_index]

    def get_staff_needed(self):
        return self.staff_needed

    def is_manager_need(self):
        return self.need_manager

    def add_worker(self, worker, shift_index):
        self.taken_places[shift_index] += 1
        self.free_places[shift_index] -= 1
        self.worker_list[shift_index].append(worker)
        worker.add_shift(shift_index, self)

    def add_worker_all(self, worker):
        available_slot = worker.get_hours_present()
        for i in range(len(self.staff_needed)):
            if available_slot[i] and self.staff_needed[i] > 0:
                self.add_worker(worker, i)

    def remove_worker(self, worker, shift_index):
        self.taken_places[shift_index] -= 1
        self.free_places[shift_index] += 1
        self.worker_list[shift_index].remove(worker)
        worker.remove_shift(shift_index)

    def display(self):
        print('{}{:.>59}'.format('Name:', self.name))
        print('{}{:.>49}'.format('Shift Duration:', str(self.shift_duration)))
        print('{}{:.>43}'.format('Stand need a manager:', str(self.need_manager)))
        print(self.staff_needed)

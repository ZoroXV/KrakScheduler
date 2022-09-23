class Stand:

    def __init__(self, name, staff_needed):
        self.name = name
        # list of free places
        self.free_places = staff_needed
        # list of taken places
        self.taken_places = [0] * len(staff_needed)
        # list that hold int that indicates the number of staff needed.
        # Length of the list will be the same of the length of the event in terms of hours. 
        # For example, an event of 4 hours will lead to a list of length 4.
        self.staff_needed = staff_needed
        # list that will hold x list containing the names of the staff
        # x will be the length of the event
        self.worker_list = []

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

    def get_worker_list(self, shift_index):
        return self.worker_list[shift_index]

    def add_worker(self, worker_name, shift_index):
        self.taken_places[shift_index] += 1
        self.free_places[shift_index] -= 1
        self.worker_list[shift_index].append(worker_name)

    def remove_worker(self, worker_name, shift_index):
        self.taken_places[shift_index] -= 1
        self.free_places[shift_index] += 1
        self.worker_list[shift_index].remove(worker_name)

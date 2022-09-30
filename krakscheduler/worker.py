class Worker:
    worker = {}

    def __init__(self, name, hours_present, manager=False, stands_priority=[]):
        self.name = name
        self.hours_present = hours_present
        self.staff_shifts = [None] * len(self.hours_present)
        self.time_worked = 0
        self.worker_stand_priority = stands_priority
        self.manager = manager

    def is_present(self):
        return self.present

    def get_name(self):
        return self.name

    def get_hours_present(self):
        return self.hours_present

    # get the duration in terms of hours that the staff will work, returns an int
    def get_presence_duration(self):
        return self.hours_present.count(1)

    def is_manager(self):
        return self.manager

    def get_staff_shifts(self):
        return self.staff_shifts

    def get_time_worked(self):
        return self.time_worked

    def get_priority(self, from_start):
        priority = 0

        for i in range(from_start + 1):
            if self.staff_shifts[i]:
                priority += 1
            else:
                priority -= 1

        return priority

    def get_worker_stand_priority(self):
        return self.worker_stand_priority

    def get_role(self):
        return self.role

    def is_working(self, shift_index):
        return self.staff_shifts[shift_index] != None

    def add_shift(self, shift_index, stand):
        self.staff_shifts[shift_index] = stand
        self.time_worked += 1

    def remove_shift(self, shift_index):
        self.staff_shifts[shift_index] = None
        self.time_worked -= 1

    def clear_shifts(self):
        self.staff_shifts = [None] * len(self.hours_present)
        self.time_worked = 0

    def display(self):
        manager_str = '(manager)' if self.manager else ''
        print(self.name + ' ' + manager_str)


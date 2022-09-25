class Worker:
    worker = {}

    def __init__(self, name, present, hours_present):
        self.name = name
        self.present = present
        self.hours_present = hours_present
        self.staff_shifts = [0] * len(self.hours_present)
        self.time_worked = 0

    # Tell if the worker will be present at the event or not
    def is_present(self):
        return self.present

    def get_name(self):
        return self.name

    def get_hours_present(self):
        return self.hours_present

    def get_staff_shifts(self):
        return self.staff_shifts

    def get_time_worked(self):
        return self.time_worked

    def is_currently_staffing(self, shift_index):
        return self.staff_shifts[shift_index] == 1

    def add_shift(self, shift_index):
        self.staff_shifts[shift_index] = 1
        self.time_worked += 1

    def remove_shift(self, shift_index):
        self.staff_shifts[shift_index] = 0
        self.time_worked -= 1
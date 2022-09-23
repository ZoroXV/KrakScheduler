class Worker:
    worker = {}

    def __init__(self, name, present):
        self.name = name
        self.present = present

    # Tell if the worker will be present at the event or not
    def is_present(self):
        return self.present

    def get_name(self):
        return self.name
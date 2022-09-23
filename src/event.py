class Event:

    def __init__(self, name, nb_stands, nb_staff, start_hour, end_hour):
        self.name = name
        self.nb_stands = nb_stands
        self.nb_staff = nb_staff
        # datetime format
        self.start_hour = start_hour
        # datetime format
        self.end_hour = end_hour
        # list that will hold stands class object
        self.stands_list = []
        # list that will hold workers class object with all their attributes
        self.staffs_list = []

    # get name of the event
    def get_name(self):
        return self.name

    def get_nb_stands(self):
        return self.nb_stands

    def get_nb_staffs(self):
        return self.nb_staff

    def get_start_hour(self):
        return self.start_hour

    def get_end_hour(self):
        return self.end_hour

    def get_event_seconds_duration(self):
        return (self.end_hour - self.start_hour).seconds
    
    def get_event_hours_duration(self):
        return int(self.get_event_seconds_duration() / 3600)

    def get_stands_list(self):
        return self.stands_list

    def get_staffs_list(self):
        return self.staffs_list

    def add_stand(self, stand):
        self.stands_list.append(stand)
        self.nb_stands +=1

    def remove_stand(self, stand):
        self.stands_list.remove(stand)
        self.nb_stands -=1

    def add_staff(self, staff):
        self.staffs_list.append(staff)
        self.nb_staff +=1

    def remove_staff(self, staff):
        self.staffs_list.remove(staff)
        self.nb_staff -=1
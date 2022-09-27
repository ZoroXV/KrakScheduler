import pytest
import datetime
import krakscheduler as ks

class TestEvent():
    def setup_class(self):
        self.start_hour = datetime.datetime(2022, 9, 10, 23, 00, 00)
        self.end_hour = datetime.datetime(2022, 9, 11, 6, 00, 00)
        self.event = ks.Event("test_event", self.start_hour, self.end_hour)
    def teardown_method(self):
        self.event.workers_list = []

    def test_get_name(self):
        assert self.event.get_name() == "test_event"

    def test_get_nb_stands(self):
        assert self.event.get_nb_stands() == 0

    def test_get_nb_workers(self):
        assert self.event.get_nb_workers() == 0

    def test_get_start_hour(self):
        assert self.event.get_start_hour() == self.start_hour

    def test_get_end_hour(self):
        assert self.event.get_end_hour() == self.end_hour

    def test_get_seconds_duration(self):
        assert self.event.get_seconds_duration() == 25200

    def test_get_hours_duration(self):
        assert self.event.get_hours_duration() == 7

    def test_get_stands_list(self):
        assert not self.event.get_stands_list()

    def test_get_workers_list(self):
        assert not self.event.get_workers_list()

    def test_get_managers(self):
        for i in range(8):
            worker = ks.Worker("worker_" + str(i), [0,1,1,1,1,0,0])
            self.event.add_worker(worker)
        assert len(self.event.get_managers()) == 0

        for i in range(2):
            worker = ks.Worker("manager_" + str(i), [0,1,1,1,1,0,0], True)
            self.event.add_worker(worker)
        assert len(self.event.get_managers()) == 2

    def test_get_stands_with_manager(self):
        assert len(self.event.get_stands_with_manager()) == 0

        stand_no_manager = ks.Stand("no_manager_stand", [1] * 7)
        self.event.add_stand(stand_no_manager)

        stand_manager = ks.Stand("manager_stand", [1] * 7, True)
        self.event.add_stand(stand_manager)

        stands = self.event.get_stands_with_manager()
        assert len(stands) == 1
        assert stands[0].get_name() == 'manager_stand'

    def test_pick_random_free_manager(self):
        manager_0 = ks.Worker("manager_0", [1]*7, True)
        self.event.add_worker(manager_0)

        manager_1 = ks.Worker("manager_1", [0,1,1,1,1,0,0], True)
        self.event.add_worker(manager_1)

        stand = ks.Stand("stand", [1]*7, True)
        stand.add_worker(manager_0, 0)

        assert manager_0.get_staff_shifts() == [1,0,0,0,0,0,0]

        free_manager = self.event.pick_random_free_manager()
        assert free_manager.get_staff_shifts() == [0,0,0,0,0,0,0]
        assert free_manager == manager_1

    def test_pick_random_free_manager_none_available(self):
        free_manager = self.event.pick_random_free_manager()
        assert free_manager is None

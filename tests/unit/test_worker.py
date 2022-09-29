import pytest
import datetime
import krakscheduler as ks

class TestWorker:
    def setup_class(self):
        self.worker = ks.Worker("Bob", [0,1,1,1,1,1,0])

    def teardown_method(self):
        self.worker.clear_shifts()

    #assert worker.get_staff_shifts()[0] == 0
    #assert worker.get_time_worked() == 0
    #assert worker.is_working(5) == 0
    #assert worker.get_presence_duration() == 5
    #assert worker.get_role() == "staff"

    def test_add_shift(self):
        self.worker.add_shift(2)
        self.worker.add_shift(5)

        assert self.worker.is_working(1) == False
        assert self.worker.is_working(2) == True
        assert self.worker.is_working(5) == True

    def test_get_shifts(self):
        assert self.worker.get_staff_shifts() == [None] * 7

    def test_get_time_worked(self):
        assert self.worker.get_time_worked() == 0

        self.worker.add_shift(2)
        self.worker.add_shift(5)
        assert self.worker.get_time_worked() == 2

    def test_remove_shift(self):
        self.worker.add_shift(2)
        assert self.worker.is_working(2) == True

        self.worker.remove_shift(2)
        assert self.worker.is_working(2) == False
        assert self.worker.get_time_worked() == 0

    def test_clear_shifts(self):
        self.worker.add_shift(3)
        self.worker.add_shift(4)
        assert self.worker.get_staff_shifts() == [0,0,0,1,1,0,0]
        assert self.worker.get_time_worked() == 2

        self.worker.clear_shifts()
        assert self.worker.get_staff_shifts() == [0,0,0,0,0,0,0]
        assert self.worker.get_time_worked() == 0

    def test_get_priority(self):
        assert self.worker.get_priority(3) == -4

        self.worker.add_shift(0)
        assert self.worker.get_priority(3) == -2

        self.worker.add_shift(1)
        self.worker.add_shift(2)
        assert self.worker.get_priority(3) == 2

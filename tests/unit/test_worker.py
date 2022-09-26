import pytest
import datetime
import krakscheduler as ks

class TestWorker:
    def setup_class(self):
        self.worker = ks.Worker("Bob", 1, [0,1,1,1,1,1,0])

    # init test structure
    worker = ks.Worker("Dylan", 1, [0,1,1,1,1,1,0])

    def test_get_staff_shifts(self):
        assert self.worker.get_staff_shifts() == [0,0,0,0,0,0,0]

    def test_add_shift(self):
        self.worker.add_shift(2)
        self.worker.add_shift(5)

        assert self.worker.is_currently_staffing(1) == False
        assert self.worker.is_currently_staffing(2) == True
        assert self.worker.is_currently_staffing(5) == True

    def test_get_time_worked(self):
        assert self.worker.get_time_worked() == 0

        self.worker.add_shift(2)
        self.worker.add_shift(5)
        assert self.worker.get_time_worked() == 2

    def test_remove_shift(self):
        self.worker.add_shift(2)
        assert self.worker.is_currently_staffing(2) == True

        self.worker.remove_shift(2)
        assert self.worker.is_currently_staffing(2) == False
        assert self.worker.get_time_worked() == 0

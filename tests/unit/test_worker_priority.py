import pytest
import datetime
import krakscheduler as ks

class TestWorkerPriority:
    def setup_class(self):
        self.worker1 = ks.Worker("W1", [1]*5)
        self.worker2 = ks.Worker("W2", [1]*5)
        self.worker3 = ks.Worker("W3", [1]*5)

        self.stand = ks.Stand("Stand", [3]*5)

        self.start_hour = datetime.datetime(2022, 9, 10, 23, 00, 00)
        self.end_hour = datetime.datetime(2022, 9, 11, 6, 00, 00)
        self.event = ks.Event("test_event", self.start_hour, self.end_hour)
        self.event.add_stand(self.stand)
        self.event.add_worker(self.worker1)
        self.event.add_worker(self.worker2)
        self.event.add_worker(self.worker3)

    def test_get_priority_basic(self):
        assert self.worker1.get_priority(0) == 0
        assert self.worker1.get_priority(1) == 1
        assert self.worker1.get_priority(2) == 3

    #def test_get_worker_multile_shift(self):
    #    self.worker1.add_shift(0, self.stand)
    #    assert self.worker1.get_priority(3) == 1

    #    self.worker1.add_shift(1, self.stand)
    #    self.worker1.add_shift(2, self.stand)
    #    assert self.worker1.get_priority(3) == -3

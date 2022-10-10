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

    def test_get_worker_basic(self):
        worker = self.event.get_available_worker(0)
        assert worker.get_priority(0) == 0


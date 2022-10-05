import pytest
import krakscheduler as ks

class TestWorkerPriority:
    def setup_class(self):
        self.worker1 = ks.Worker("W1", [1]*5)
        self.worker2 = ks.Worker("W2", [1]*5)
        self.worker3 = ks.Worker("W3", [1]*5)
        self.worker4 = ks.Worker("W4", [1]*5)
        self.worker5 = ks.Worker("W5", [1]*5)

        self.stand = ks.Stand("Stand", [5]*5)

    def test_get_worker_basic(self):
        assert True

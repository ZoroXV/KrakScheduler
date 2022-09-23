import pytest
import datetime
import krakscheduler as ks

class TestEvent():
    def setup_class(self):
        self.start_hour = datetime.datetime(2022, 9, 10, 23, 00, 00)
        self.end_hour = datetime.datetime(2022, 9, 11, 6, 00, 00)
        self.event = ks.Event("test_event", 0, 0, self.start_hour, self.end_hour)

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

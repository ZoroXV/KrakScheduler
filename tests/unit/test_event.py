import pytest
import datetime
import krakscheduler as ks

def test_get_name():
    start_hour = datetime.datetime(2022, 9, 10, 23, 00, 00)
    end_hour = datetime.datetime(2022, 9, 11, 6, 00, 00)
    event = ks.Event("test_event", 0, 0, start_hour, end_hour)

    assert event.get_name() == "test_event"

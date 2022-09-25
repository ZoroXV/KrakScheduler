import pytest
import datetime
import krakscheduler as ks

def test_worker_class():

    # init test structure
    worker = ks.Worker("Dylan", 1, [0,1,1,1,1,1,0])

    # basic test
    assert worker.is_present() == 1
    assert worker.get_name() == "Dylan"
    assert worker.get_hours_present()[6] == 0
    assert worker.get_hours_present()[5] == 1
    assert worker.get_staff_shifts()[0] == 0
    assert worker.get_time_worked() == 0
    assert worker.is_currently_staffing(5) == 0

    # Add shift
    worker.add_shift(2)
    worker.add_shift(5)

    assert worker.is_currently_staffing(1) == False
    assert worker.is_currently_staffing(2) == True
    assert worker.is_currently_staffing(5) == True

    assert worker.get_time_worked() == 2

    # Remove shift
    worker.remove_shift(2)

    assert worker.is_currently_staffing(2) == False
    assert worker.get_time_worked() == 1

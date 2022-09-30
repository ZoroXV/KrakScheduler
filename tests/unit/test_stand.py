from re import A
import pytest
import datetime
import krakscheduler as ks

def test_stand_class():

    # init test structure
    bar_stand = ks.Stand("bar_stand", [8,6,6,6,4,4,4])

    # basic test
    assert bar_stand.get_name() == "bar_stand"
    assert bar_stand.get_places(0) == 8
    assert bar_stand.get_free_places(0) == 8
    assert bar_stand.get_taken_places(0) == 0

    assert len(bar_stand.get_specific_shift_worker_list(0)) == 0

    ## Add staff on stand
    worker = ks.Worker("Dylan", [0,1,1,1,1,1,0])

    bar_stand.add_worker(worker, 1)

    assert len(bar_stand.get_specific_shift_worker_list(1)) != 0
    assert bar_stand.get_specific_shift_worker_list(1)[0].get_name() == "Dylan"

    assert bar_stand.get_free_places(1) == 5
    assert bar_stand.get_taken_places(1) == 1

    assert worker.is_working(1) == True
    assert worker.get_staff_shifts()[1] == bar_stand
    assert worker.get_time_worked() == 1

    ## Remove staff
    bar_stand.remove_worker(worker, 1)

    assert len(bar_stand.get_specific_shift_worker_list(1)) == 0

    assert bar_stand.get_free_places(1) == 6
    assert bar_stand.get_taken_places(1) == 0

    assert worker.is_working(1) == False
    assert worker.get_staff_shifts()[1] == None
    assert worker.get_time_worked() == 0

def test_add_worker_all():
    stand = ks.Stand("stand", [8,6,6,6,4,4,4])
    worker = ks.Worker("Dylan", [0,1,1,0,0,0,0])

    assert worker.get_staff_shifts() == [None] * len(worker.get_hours_present())

    stand.add_worker_all(worker)

    assert worker.get_staff_shifts() == [None,stand,stand,None,None,None,None]

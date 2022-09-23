from xlsx_builder import *
import xlsxwriter
from scheduler import Scheduler
from event import Event
from stand import Stand
from worker import Worker
import datetime

def main():

    start_hour = datetime.datetime(2022, 9, 10, 23, 00, 00)
    end_hour = datetime.datetime(2022, 9, 11, 6, 00, 00)
    event = Event("kraken_awakening", 0, 0, start_hour, end_hour)
    entry_stand = Stand("entry_stand",  [6,6,6,6,0,0,0])
    bar_stand = Stand("bar_stand", [8,6,6,6,4,4,4])
    food_stand = Stand("food_stand",  [3,3,3,3,3,3,3])
    loundry_stand = Stand("loundry_stand", [4,4,4,2,2,4,4])
    photo_stand = Stand("photo_stand", [2,2,2,2,0,0,0])
    toilet_stand = Stand("toilet_stand", [2,2,2,2,2,2,2])

    list_workers = []
    for i in range(42):
        worker = Worker("worker_" + str(i),1)
        list_workers.append(worker)
        event.add_staff(worker)


    event.add_stand(entry_stand)
    event.add_stand(bar_stand)
    event.add_stand(food_stand)
    event.add_stand(loundry_stand)
    event.add_stand(photo_stand)
    event.add_stand(toilet_stand)


    print(event.get_name())
    print(event.get_nb_stands())
    print(event.get_nb_staffs())


    wb, global_sheet, _ = build_schedule(event)

    #scheduler = Scheduler(event)
    #scheduler.fill_schedule()
#
    #schedule = scheduler.get_schedule()
    #print(schedule)
    #fill_global_sheet(global_sheet, len(time_slots), schedule)

    wb.close()
    
    

    datetime1 = datetime.datetime(2022,3,8,0,0,0)
    datetime2 = datetime.datetime(2022,3,8,12,30,0)

    print(datetime1 - datetime2)

if __name__ == '__main__':
    main()
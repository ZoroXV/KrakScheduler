import krakscheduler as ks
import datetime

def main():
    start_hour = datetime.datetime(2022, 9, 10, 23, 00, 00)
    end_hour = datetime.datetime(2022, 9, 11, 6, 00, 00)
    event = ks.Event("kraken_awakening", 0, 0, start_hour, end_hour)
    entry_stand = ks.Stand("entry_stand",  [6,6,6,6,0,0,0])
    bar_stand = ks.Stand("bar_stand", [8,6,6,6,4,4,4])
    food_stand = ks.Stand("food_stand",  [3,3,3,3,3,3,3])
    loundry_stand = ks.Stand("loundry_stand", [4,4,4,2,2,4,4])
    photo_stand = ks.Stand("photo_stand", [2,2,2,2,0,0,0])
    toilet_stand = ks.Stand("toilet_stand", [2,2,2,2,2,2,2])

    list_workers = []
    for i in range(42):
        worker = ks.Worker("worker_" + str(i), 1, [0,1,1,1,1,0,0])
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


    scheduler = ks.Scheduler(event)
    #scheduler.fill_schedule()
    #schedule = scheduler.get_schedule()
    print(scheduler.get_current_shift_remaining_places(3, entry_stand))
    #print(schedule)
    print(scheduler.get_current_shift_remaining_places(1, bar_stand))
    #fill_global_sheet(global_sheet, len(time_slots), schedule)
    print(scheduler.get_current_shift_worker_list(1, bar_stand))

    wb, global_sheet, _ = ks.build_schedule(scheduler)



    wb.close()

if __name__ == '__main__':
    main()

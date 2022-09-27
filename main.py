import krakscheduler as ks
import datetime

def main():
    event = ks.build_event()

    for i in range(42):
        worker = ks.Worker("worker_" + str(i), [0,1,1,1,1,0,0])
        event.add_worker(worker)

    #Init Stand Manager
    for stand in event.get_stands_list():
        worker = ks.Worker(stand.get_name() + "_manager", [0,1,1,1,1,0,0], True)
        event.add_worker(worker)

    event.display()

    scheduler = ks.Scheduler(event)
    scheduler.fill_schedule()
    scheduler.display()

    wb, global_sheet, _ = ks.build_schedule(scheduler)

    wb.close()

if __name__ == '__main__':
    main()

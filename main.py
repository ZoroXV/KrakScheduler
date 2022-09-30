import krakscheduler as ks
import datetime

def main():
    event = ks.build_event()

    for i in range(20):
        worker = ks.Worker("worker_" + str(i), [0,1,1,1,1,0,0])
        event.add_worker(worker)

    for i in range(20, 40):
        worker = ks.Worker("worker_" + str(i), [1,1,0,0,1,1,1])
        event.add_worker(worker)

    #Init Stand Manager
    for i in range(len(event.get_stands_list())):
        worker = ks.Worker("manager_" + str(i), [1,1,1,1,1,1,1], True)
        event.add_worker(worker)

    event.display()

    scheduler = ks.Scheduler(event)
    scheduler.fill_schedule()
    scheduler.display_global()

    wb, global_sheet, _ = ks.build_schedule(scheduler)

    wb.close()

if __name__ == '__main__':
    main()

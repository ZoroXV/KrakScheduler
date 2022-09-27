import krakscheduler as ks
import datetime

def main():
    event = ks.build_event()

    list_workers = []
    for i in range(20):
        worker = ks.Worker("worker_" + str(i), 1, [0,1,1,1,1,0,0])
        list_workers.append(worker)
        event.add_worker(worker)

    event.display()

    scheduler = ks.Scheduler(event)
    scheduler.fill_schedule()

    wb, global_sheet, _ = ks.build_schedule(scheduler)

    wb.close()

if __name__ == '__main__':
    main()

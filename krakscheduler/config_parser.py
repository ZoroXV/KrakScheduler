import yaml
import krakscheduler as ks

from datetime import datetime

def load_config_file(filename):
    with open(filename) as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as exc:
            print(exc)

def build_event(filename = 'event-config.yml'):
    data = load_config_file(filename)

    time = data['time']
    start_date = datetime.strptime(time['start'], '%d-%m-%Y %H:%M')
    end_date = datetime.strptime(time['end'], '%d-%m-%Y %H:%M')

    event = ks.Event(data['name'], start_date, end_date)

    stands = data['stands']
    for _, stand in stands.items():
        need_manager = False
        if 'need_manager' in stand.keys():
            need_manager = True
        stand = ks.Stand(stand['name'], stand['workers'][0], need_manager)
        event.add_stand(stand)

    return event

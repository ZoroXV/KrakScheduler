import yaml
import krakscheduler as ks

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
    event = ks.Event(data['name'], time['start'], time['end'])

    stands = data['stands']
    for _, stand in stands.items():
        stand = ks.Stand(stand['name'], stand['workers'][0])
        event.add_stand(stand)

    return event

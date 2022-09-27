# KrakScheduler

## Usage
To use KrakScheduler you have to configure your event with a YAML file.
You also need to give a CSV file (not implemented yet) to fill the workers list available to fill the schedule.

### Event Config File Template
Following this sentence you will find a template for the config file.
```yaml
---
name: <Your Event Name>
time:
  start: <DD-MM-YYYY HH:MM>
  end: <DD-MM-YYYY HH:MM>
stands:
  0:
    name: <Stand Name>
    <Optional> need_manager: True
    workers:
      - [X,X,X,X,X,X,X]
```


### Setup Dev Environement
You need to build the python package first.
To achieve this you can use the Makefile with `init` task or do the following command:
```
pip install -e .
```

### Makefile
A Makefile is provided for an easier use. The available tasks are:
- `all`: Run the testsuite and then launch python application
- `run`: Run the python application
- `init`: Build and install locally the KrakenScheduler Package
- `check`: Run the testsuite
- `clean`: Remove generated files and build artifacts

## Implemented Features

## Further Features
Checked item will be in the 0.1 release

- [X] Create a schedule for Kraken's Events
- [X] Produce a xlsx file with global and individual view of the planning
- [X] Fill each stand with correct number of workers during all the event
- [X] Make worker not duplicate in multiple stand for one time slot
- [X] Use a config (yml or json) file to configure the current event we want to schedule
  - Define the begin time of the event
  - Define stands needed for the event
  - Define workers needed each hour for stands
- [X] Possibility to define different quantity of workers needed on a stand for each time slot
- [X] Stand can required a manager or not
- [X] Worker can be a manager
- [ ] Add the posibility to give a break during the event for each worker
- [ ] Add colors and style in the produced xlsx

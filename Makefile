all: check run

run:
	@python main.py

init:
	@pip install -e .

check:
	@pytest

clean:
	@pip uninstall -y krakscheduler
	@rm -rf dist/
	@rm -rf krakscheduler.egg-info/
	@rm -rf krakscheduler/__pycache__/
	@rm -rf krakscheduler/xlsx_builder/__pycache__/
	@rm -rf tests/unit/__pycache__/
	@rm -rf .pytest_cache/
	@rm schedule.xlsx

.PHONY:
	run
	init
	check
	clean

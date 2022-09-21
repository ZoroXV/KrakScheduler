all: check run

run:
	@python src/__init__.py

init:
	@pip install -r requirements.txt

check:
	@python tests/unit/__init__.py -v

clean:
	@rm -rf src/__pycache__/
	@rm -rf tests/unit/__pycache__/
	@rm schedule.xlsx

.PHONY:
	run
	init
	check
	clean

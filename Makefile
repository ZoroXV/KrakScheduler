all: run

run:
	@python src/__init__.py

init:
	@pip install -r requirements.txt

check:
	@echo "Running Tests..."

clean:
	@rm -rf src/__pycache__/

.PHONY:
	run
	init
	check
	clean

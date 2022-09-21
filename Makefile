init:
	pip install -r requirements.txt

check:
	@echo "Running Tests..."

.PHONY:
	init
	check

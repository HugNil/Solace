
#Use your version of python
PYTHON ?= python

------------------------------------

#The directory of the code
SRC_DIR := src

------------------------------------

#The file where the code program runs
MAIN_FILE := $(SRC_DIR)/gui.py

------------------------------------

#Commands:
.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: run
run:
	$(PYTHON) $(MAIN_FILE)

.PHONY: clean
clean:
	rm -rf __pycache__

.PHONY: test
test:
	$(PYTHON) -m pytest $(SRC_DIR)

.PHONY: help

------------------------------------

#How to use these commands with make
help:
	@echo "Usage: make <target>"
	@echo "  install  - Install dependencies"
	@echo "  run      - Run the Solace application"
	@echo "  clean    - Clean up generated files"
	@echo "  test     - Run automated tests (not configured)"
	@echo "  help     - Show this help message" 

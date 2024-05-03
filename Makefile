
#Use your version of python
PYTHON ?= python

# ------------------------------------

#The directory of the code
SRC_DIR := src
TEST_DIR := tests
# ------------------------------------

#The file where the code program runs
MAIN_FILE := $(SRC_DIR)/gui.py

# ------------------------------------

# Print out colored action message
define MESSAGE
	@echo "--> $(1)"
endef

# ------------------------------------

#Commands:
.PHONY: install
install:
	@$(call MESSAGE, Installing dependencies...)
	pip install -r requirements.txt


.PHONY: run
run:
	@$(call MESSAGE, Running the Solace application...)
	$(PYTHON) $(MAIN_FILE)


.PHONY: clean
clean:
	@$(call MESSAGE, Cleaning up...)
	rm -rf __pycache__


.PHONY: test
test:
	@$(call MESSAGE, Running pytest and creating a coverage report...)
	@coverage run -m pytest $(TEST_DIR)
	@coverage report -m
	@coverage html


.PHONY: help


# ------------------------------------


#How to use these commands with make
help:
	@echo "Usage: make <target>"
	@echo "  install  - Install dependencies"
	@echo "  run      - Run the Solace application"
	@echo "  clean    - Clean up generated files"
	@echo "  test     - Run automated tests (not configured)"
	@echo "  help     - Show this help message"
PYTHON ?= python3
ENTRY ?= battle.py
ARGS ?=
SOURCES = $(wildcard *.py ex*/*.py ex*/*/*.py alchemy/*.py alchemy/*/*.py)

all: check

check:
	$(PYTHON) -m py_compile $(SOURCES)

run:
	$(PYTHON) $(ENTRY) $(ARGS)

.PHONY: all check run

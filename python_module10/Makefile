PYTHON ?= python3
ENTRY ?= ex0/lambda_spells.py
ARGS ?=
SOURCES = $(wildcard *.py ex*/*.py ex*/*/*.py alchemy/*.py alchemy/*/*.py)

all: check

check:
	$(PYTHON) -m py_compile $(SOURCES)

run:
	$(PYTHON) $(ENTRY) $(ARGS)

.PHONY: all check run

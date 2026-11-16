UV ?= uv
TEST_PYTHON ?= 3.12
TEST_ARGS ?=

.PHONY: test
test:
	MPLBACKEND=Agg $(UV) run --no-project --python $(TEST_PYTHON) \
		--with-requirements requirements-test.txt \
		python -m pytest tests -v $(TEST_ARGS)

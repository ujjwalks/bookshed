.PHONY: tests

BASH ?= /bin/bash

DC_COMMAND = docker-compose
DC_UP_COMMAND = $(DC_COMMAND) up
DC_RUN_COMMAND = $(DC_COMMAND) run --rm
PYTEST_CMD = pytest

EXTRA ?=
FAIL_FAST ?= -x
LOOP ?= -f --ff
NOT_SLOW ?= -m "not slow"

# Helpers
c ?= web
C ?= $(c)

## General targets
build:
	$(DC_COMMAND) build

web:
	$(DC_UP_COMMAND) web

bash:
	$(DC_RUN_COMMAND) --no-deps $(C) $(BASH)

stop:
	$(DC_COMMAND) stop

logs:
	$(DC_COMMAND) logs -f --tail=30

## Clean up targets
# using -j > 1 makes it parallel :D
clean:
	@sudo $(MAKE) -j 3 clean-pyc clean-build clean-coverage

clean-build:
	rm -fr *.egg-info
	rm -fr .cache/
	rm -fr build/
	rm -fr dist/

clean-coverage:
	rm -rf .coverage
	rm -rf .coverage.*
	rm -rf .instrumental.cov

clean-pyc:
	-find . -name '*.pyc' -exec rm -f {} +
	-find . -name '*.pyo' -exec rm -f {} +
	-find . -name '*~' -exec rm -f {} +
	-find . -name '__pycache__' -exec rm -fr {} +

## Test targets
tests:
	$(DC_RUN_COMMAND) tests $(PYTEST_CMD) $(EXTRA)

fast-tests:
	$(DC_RUN_COMMAND) tests $(PYTEST_CMD) \
		$(NOT_SLOW) \
		$(FAIL_FAST) \
		$(EXTRA)

# Will start an ipdb session on failing test
ipdb-tests:
	$(DC_RUN_COMMAND) tests $(PYTEST_CMD) --pdb --pdbcls=IPython.terminal.debugger:TerminalPdb -s $(EXTRA)

tests-loop:
	$(DC_RUN_COMMAND) tests $(PYTEST_CMD) \
		$(LOOP) \
		$(NOT_SLOW) \
		$(FAIL_FAST) \
		$(EXTRA)

## Non-test targets
nuke:
	docker rm -f $$(docker ps -aqf "name=moviegraph") || echo $$'No containers to remove.'

py3-compatibility:
	$(DC_RUN_COMMAND) --no-deps tests caniusepython3 -v -r \
		requirements/base.txt \
		requirements/classifier.txt \
		requirements/matplotlib.txt \
		requirements/prereqs.txt \
		requirements/tests.txt

outdated-dependencies:
	$(DC_RUN_COMMAND) --no-deps tests pip list -o --format=columns

SHELL := /bin/bash

lint:
	flake8

test:
	python -m pytest

build:
	$(MAKE) lint
	$(MAKE) test

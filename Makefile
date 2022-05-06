SHELL := /bin/bash

lint:
	flake8

test:
	python -m pytest

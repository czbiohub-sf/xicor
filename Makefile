PYTHON ?= python

clean:
	$(PYTHON) setup.py clean --all

install:
	$(PYTHON) setup.py install

dist: FORCE
	$(PYTHON) setup.py sdist

test:
	pip install -e '.[test]'
	$(PYTHON) -m pytest

coverage:
	$(PYTHON) setup.py clean --all
	$(PYTHON) -m pytest --cov=. --cov-report term-missing

FORCE:
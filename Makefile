.PHONY: test testcov release dist clean

RM = rm -rf

# `pytest` and `python -m pytest` are equivalent, except that the latter will
# add the current working directory to sys.path. We don't want that; we want
# to test against the _installed_ package(s), not against any python sources
# that are (accidentally) in our CWD.
PYTEST = python setup.py test --verbose

# The ?= operator below assigns only if the variable isn't defined yet. This
# allows the caller to override them:
#
#     TESTS=other_tests make test
#
#PYTEST_OPTS    ?= -p no:cacheprovider --exitfirst --capture=no
PYTEST_OPTS     ?= -p no:cacheprovider --exitfirst
PYTEST_OPTS_COV ?= -p no:cacheprovider --exitfirst --cov=src --cov-report=term --no-cov-on-fail
TESTS ?= tests


PYTHON = python3
RM = rm -rf

dist: test clean
	$(PYTHON) setup.py sdist


release: test clean
	$(PYTHON) setup.py sdist upload


build:
	$(PYTHON) setup.py build


test:
	$(PYTEST) --addopts "$(PYTEST_OPTS) $(TESTS)"


testcov:
	$(PYTEST) $(PYTEST_OPTS_COV) $(TESTS)


clean:
	@$(RM) .cache .coverage .eggs src/datapunt_config_loader.egg-info
	@find . \( \
		    -iname "*~" \
		-or -iname ".DS_Store" \
        -or -iname "*.pyc" \
		-or -iname "__pycache__" \
		-or -iname "Desktop.ini" \
		-or -iname "Thumbs.db" \
		-or -iname "__MACOSX__" \
	\) -delete

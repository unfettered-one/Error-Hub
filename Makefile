PYTHON=python
PYTEST=pytest
PYLINT=pylint
PYTHONPATH=errorhub/errorhub


lint:
	$(PYLINT) $(PYTHONPATH) --verbose
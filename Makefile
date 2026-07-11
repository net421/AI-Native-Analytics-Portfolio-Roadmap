.PHONY: validate test verify

validate:
	python tools/validate_portfolio.py

test:
	python -m unittest discover -s tests -v

verify: validate test

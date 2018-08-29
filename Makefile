.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  test    Runs unit tests."
	@echo "  lint    Runs linters."

.PHONY: test
test:
	@py.test --cov=method_override tests

.PHONY: lint
lint:
	@flake8 method_override tests

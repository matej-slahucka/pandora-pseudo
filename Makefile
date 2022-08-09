.PHONY: format mypy pylint

format:
	poetry run black src
	poetry run isort src

mypy:
	poetry run mypy src

pylint:
	poetry run pylint src

.PHONY: compile-dev install-dev format

REQUIREMENTS_PATH=requirements
REQUIREMENTS=requirements
REQUIREMENTS_DEV=requirements-dev

compile-dev:
	cd ${REQUIREMENTS_PATH} && pip-compile --output-file=${REQUIREMENTS_DEV}.txt ${REQUIREMENTS_DEV}.in

install-dev:
	pip install -r ${REQUIREMENTS_PATH}/${REQUIREMENTS_DEV}.txt

format:
	black src
	isort src

mypy:
	mypy src

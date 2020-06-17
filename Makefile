t:
	python3 -m pytest

p:
	pre-commit run --all-files

build:
	python3 setup.py sdist bdist_wheel
	twine check dist/*

freeze:
	pip freeze > requirements.txt

t:
	python3 -m pytest

p:
	black *.py
	mypy *.py

build:
	python3 setup.py sdist bdist_wheel
	twine check dist/*

freeze:
	pip freeze > requirements.txt

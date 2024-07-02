#!/usr/bin/env python3

install:
	poetry install

lock:
	poetry lock

up-dev:
	python3 manage.py runserver 8000

migrations:
	python3 manage.py makemigrations --name $(name)

migrate:
	python3 manage.py migrate

test:
	python3 manage.py test

test-coverage:
	coverage run --source='.' manage.py test task_manager
	coverage report -m
	coveralls



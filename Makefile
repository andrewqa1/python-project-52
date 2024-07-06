#!/usr/bin/env python3

install:
	poetry install

lock:
	poetry lock

up-prod:
	poetry run python3 manage.py runserver 8000 --noreload

up-dev:
	poetry run python3 manage.py runserver 8000

migrations:
	poetry run python3 manage.py makemigrations --name $(name)

migrate:
	poetry run python3 manage.py migrate

test:
	poetry run python3 manage.py test

test-coverage:
	poetry run coverage run --source='.' manage.py test task_manager
	poetry run coverage report -m
	poetry run coveralls

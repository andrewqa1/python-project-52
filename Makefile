#!/usr/bin/env python3

install:
	poetry install

lock:
	poetry lock

up-dev:
	python3 manage.py runserver 8000

migrations:
	python manage.py makemigrations --name $(name)

migrate:
	python manage.py migrate

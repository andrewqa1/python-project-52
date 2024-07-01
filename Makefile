#!/usr/bin/env python3

install:
	poetry install

lock:
	poetry lock

up-dev:
	python3 ./task_manager/manage.py runserver 8000

migrations:
	python3 ./task_manager/manage.py makemigrations --name $(name)

migrate:
	python3 ./task_manager/manage.py migrate

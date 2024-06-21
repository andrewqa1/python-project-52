#!/usr/bin/env python3

install:
	poetry install

lock:
	poetry lock

up-dev:
	python3 manage.py runserver 8000

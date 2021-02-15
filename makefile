# sudo docker-compose run web django-admin startproject composeexample .
# sudo docker-compose run web django-admin startapp vscode_info
# sudo chown -R $USER:$USER .
# sudo docker-compose run web django-admin makemigrations

SHELL := /bin/bash

up:
	sudo docker-compose up

down:
	sudo docker-compose down

m:
	sudo docker-compose run web python3 manage.py migrate
mm:
	sudo docker-compose run web python3 manage.py makemigrations 
run:
	python3 manage.py runserver

freeze:
	sudo docker-compose run web pip install -r requirements.txt 

pip_install:
	sudo docker-compose run web pip install -r requirements.txt 

build:
	sudo docker-compose build

test:
	sudo docker-compose run web pytest

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

dummy:
	sudo docker-compose run web python3 manage.py generate_test_db

super:
	sudo docker-compose run web python3 manage.py generate_supers

flush:
	sudo docker-compose run web python3 manage.py flush 

delete_migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	# sudo docker-compose run web python3 manage.py makemigrations
	# sudo docker-compose run web python3 manage.py migrate --run-syncdb

showmigrations:
	sudo docker-compose run web python3 manage.py showmigrations
	
reset_db:
	sudo docker-compose run web python3 manage.py reset_db


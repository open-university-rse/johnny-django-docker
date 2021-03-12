# sudo docker-compose run web django-admin startproject composeexample .
# sudo docker-compose run web django-admin startapp vscode_info
# sudo chown -R $USER:$USER .
# sudo docker-compose run web django-admin makemigrations
# python manage.py runscript delete_all_questions
# http://0.0.0.0:8000/history
# http://0.0.0.0:8000/clipboard

# API destinations
# http://0.0.0.0:8000/api/website/
# http://0.0.0.0:8000/api/clipboard/
# http://0.0.0.0:8000/api/file/


SHELL := /bin/bash

up:
	sudo docker-compose up --remove-orphans

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
	sudo docker-compose run web pytest -s -v

dummy:
	sudo docker-compose run web python3 manage.py generate_test_db

super:
	sudo docker-compose run web python3 manage.py runscript generate_supers

flush:
	sudo docker-compose run web python3 manage.py flush 

delete_migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	sudo docker-compose run web python3 manage.py makemigrations
	sudo docker-compose run web python3 manage.py migrate 

showmigrations:
	sudo docker-compose run web python3 manage.py showmigrations
	
reset_db:
	sudo docker-compose run web python3 manage.py reset_db

reset:
	sudo docker-compose run web python3 manage.py reset_db
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	sudo docker-compose run web python3 manage.py makemigrations 
	sudo docker-compose run web python3 manage.py migrate auth
	sudo docker-compose run web python3 manage.py migrate files
	sudo docker-compose run web python3 manage.py migrate
	sudo docker-compose run web python3 manage.py migrate --run-syncdb

pyclean:
	find . -regex '^.*\(__pycache__\|\.py[co]\)$' -delete

test_message:
	sudo docker-compose run web python3 manage.py runscript send_test_debug_message

user:
	sudo chown -R $USER:$USER .


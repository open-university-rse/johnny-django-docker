import platform
from doit.tools import LongRunning

DOCKER = "docker-compose"
VERBOSITY_LEVEL = 2
MANAGE_PY = "sudo " + DOCKER + " run web python3 manage.py "
OS_CMD_SEP = " & " if platform.system() == "Windows" else "; "


def task_up():
    cmd = "sudo " + DOCKER + " up --remove-orphans"
    return {"actions": [LongRunning(cmd)], "verbosity": VERBOSITY_LEVEL}


def task_down():
    cmd = "sudo " + DOCKER + " down"
    return {"actions": [cmd], "verbosity": VERBOSITY_LEVEL}


def task_user():
    return {"actions": ["sudo chown -R $USER:$USER ."]}


def task_pip_install():
    cmd = "sudo " + DOCKER + " run web pip install -r requirements.txt"
    return {"actions": [cmd], "verbosity": VERBOSITY_LEVEL}


def task_m():
    cmd = MANAGE_PY + "migrate"
    return {"actions": [cmd], "verbosity": VERBOSITY_LEVEL}


def task_mm():
    cmd = MANAGE_PY + "makemigrations"
    return {"actions": [cmd], "verbosity": VERBOSITY_LEVEL}


def task_build():
    cmd = "sudo " + DOCKER + " build"
    return {"actions": [cmd], "verbosity": VERBOSITY_LEVEL}


def task_test():
    cmd = "sudo " + DOCKER + " run web pytest -s -v"
    return {"actions": [cmd], "verbosity": VERBOSITY_LEVEL}


def task_dummy():
    cmd = MANAGE_PY + "generate_test_db"
    return {"actions": [cmd], "verbosity": VERBOSITY_LEVEL}


def task_super():
    cmd = "sudo " + DOCKER + " run web python3 manage.py runscript generate_supers"
    return {"actions": [cmd], "verbosity": VERBOSITY_LEVEL}


# sudo docker-compose run web python3 manage.py reset_db
# 	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# 	find . -path "*/migrations/*.pyc"  -delete
# 	find . -path "*.sqlite3"  -delete
# 	sudo docker-compose run web python3 manage.py makemigrations
# 	sudo docker-compose run web python3 manage.py migrate auth
# 	sudo docker-compose run web python3 manage.py migrate files
# 	sudo docker-compose run web python3 manage.py migrateimport platform
# 	sudo docker-compose run web python3 manage.py migrate --run-syncdb


def task_reset():
    cmd = (
        MANAGE_PY
        + "reset_db"
        + OS_CMD_SEP
        + 'find . -path "*/migrations/*.py" -not -name "__init__.py" -delete'
        + OS_CMD_SEP
        + 'find . -path "*/migrations/*.pyc" -delete'
        + OS_CMD_SEP
        + 'find . -path "*.sqlite3" -delete'
        + OS_CMD_SEP
        + MANAGE_PY
        + "makemigrations"
        + OS_CMD_SEP
        + MANAGE_PY
        + "migrate --run-syncdb"
        + OS_CMD_SEP
    )

    return {"actions": [cmd], "verbosity": VERBOSITY_LEVEL}

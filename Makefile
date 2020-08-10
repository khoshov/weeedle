VENV_NAME?=venv
PIP=$(VENV_NAME)/bin/pip
PYTHON=${VENV_NAME}/bin/python3
PROJECT_NAME?=app
USERID := $$(id -u)
GROUPID := $$(id -g)
DOCKERCOMPOSE := CURRENT_UID=$(USERID):$(GROUPID) docker-compose -f docker-compose.yml

up:
	${DOCKERCOMPOSE} up

showmigrations:
	${DOCKERCOMPOSE} run --rm web python src/manage.py showmigrations --settings=config.settings

makemigrations:
	${DOCKERCOMPOSE} run --rm web python src/manage.py makemigrations ${app} --settings=config.settings

migrate:
	${DOCKERCOMPOSE} run --rm web python src/manage.py migrate --settings=config.settings

compilescss:
	${DOCKERCOMPOSE} run --rm web python src/manage.py compilescss --settings=config.settings

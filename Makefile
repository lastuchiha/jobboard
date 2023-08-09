APP = jobboard
PREFIX = python ${APP}/manage.py

.PHONY: migrations migrate server superuser %-req shell

migrations:
	${PREFIX} makemigrations

migrate:
	${PREFIX} migrate 

server:
	${PREFIX} runserver

superuser:
	${PREFIX} createsuperuser

%-req:
	pip freeze > ${APP}/requirements/$*.txt

shell:
	${PREFIX} shell
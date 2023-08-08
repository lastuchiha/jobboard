PREFIX = python jobboard/manage.py 

migrations:
	${PREFIX} makemigrations

migrate:
	${PREFIX} migrate 

server:
	${PREFIX} runserver

superuser:
	${PREFIX} createsuperuser
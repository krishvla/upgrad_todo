web: gunicorn upgrad_project.wsgi --log-file -

worker: celery worker --app=upgrad_project.celery --loglevel=info


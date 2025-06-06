#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py create_admin
python manage.py check_admin
gunicorn core.wsgi:application --bind 0.0.0.0:$PORT

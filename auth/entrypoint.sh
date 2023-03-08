#!/bin/bash

echo "----- Collect static files ------ " 
python manage.py collectstatic --noinput

echo "-----------Apply migration--------- "
python manage.py makemigrations 
python manage.py migrate


if [ "$1" = "develop" ]; then
    exec python3 manage.py runserver 0.0.0.0:8000
else
    exec gunicorn auth.wsgi:application --bind 0.0.0.0:8000
fi
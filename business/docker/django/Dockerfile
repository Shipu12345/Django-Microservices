FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update
RUN apt-get install vim -y

WORKDIR /app
COPY . /app/

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod 755 entrypoint.sh

RUN ls -la

RUN ["chmod", "+x", "/app/entrypoint.sh"]
# ENTRYPOINT [ "python3", "manage.py", "runserver" ]
# ENTRYPOINT [ "gunicorn", "business.wsgi:application", "--workers", "2", "--bind", "0.0.0.0:8000" ]
ENTRYPOINT ["/app/entrypoint.sh", "develop"]
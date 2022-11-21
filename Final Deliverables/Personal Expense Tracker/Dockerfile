FROM python:latest
COPY ./app /app
COPY ./requirements.txt /requirements.txt
WORKDIR /app
RUN pip install -r /requirements.txt
RUN cd /app
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py migrate --run-syncdb
EXPOSE 8000
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]
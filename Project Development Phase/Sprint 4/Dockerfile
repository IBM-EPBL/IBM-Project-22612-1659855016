FROM python:3.6
WORKDIR /Sprint 4
ADD . /Sprint 4
COPY requirements.txt /Sprint 4
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000
CMD ["python","manage.py", "migrate"]
CMD ["python","manage.py", "runserver"]
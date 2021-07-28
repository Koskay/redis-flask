FROM python:3.8.5

WORKDIR /app

ENV FLASK_APP = flask_app.py

ENV FLASK_RUN_HOST = 0.0.0.0

RUN apt-get update -y

RUN apt-get install -y python-pip python-dev build-essential

COPY ./requirements.txt /app/requirements.txt

EXPOSE 5000

RUN pip3 install -r requirements.txt

COPY ./app/flask_app.py /app/flask_app.py

ENTRYPOINT [ "python" ]

CMD [ "flask_app.py" ]


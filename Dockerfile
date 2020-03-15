FROM python:3

WORKDIR /app

RUN pip install flask psycopg2 flask-cors

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["run.py"]

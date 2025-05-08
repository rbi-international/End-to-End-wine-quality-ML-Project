FROM python:3.10.17-alpine3.20


WORKDIR /app


COPY . /app


RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
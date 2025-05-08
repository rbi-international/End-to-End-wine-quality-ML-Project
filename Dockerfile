FROM python:3.10.17-slim-bullseye

WORKDIR /app

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy application code
COPY . /app/

CMD ["python3", "app.py"]
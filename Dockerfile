FROM python:3.10.17-slim-bullseye

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install wheel
RUN pip install --upgrade pip wheel setuptools

# Copy requirements files
COPY requirements-base.txt /app/
COPY requirements.txt /app/

# Install base requirements first
RUN pip install --no-cache-dir -r requirements-base.txt

# Copy all code
COPY . /app/

# Install in editable mode
RUN pip install -e .

CMD ["python3", "app.py"]
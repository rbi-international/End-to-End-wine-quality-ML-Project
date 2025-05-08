FROM python:3.10.17-alpine3.20

WORKDIR /app

# Install build dependencies for scientific packages
RUN apk add --no-cache \
    build-base \
    gcc \
    g++ \
    gfortran \
    musl-dev \
    openblas-dev \
    lapack-dev \
    python3-dev

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements and install
COPY requirements.txt .

# Install packages with pre-built wheels when possible
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copy application code
COPY . .

CMD ["python3", "app.py"]
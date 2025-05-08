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

# Upgrade pip, setuptools, and wheel
RUN pip install --upgrade pip setuptools wheel

# Create a requirements file without the -e . line
COPY requirements.txt /app/
RUN grep -v "^-e" requirements.txt > requirements_temp.txt

# Install most dependencies first
RUN pip install --no-cache-dir -r requirements_temp.txt

# Copy the rest of the application
COPY . /app/

# Finally install the package in editable mode
RUN pip install -e .

CMD ["python3", "app.py"]
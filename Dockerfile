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

# Copy requirements and install without the -e . line
COPY requirements.txt .
RUN pip install --no-cache-dir notebook==7.0.6 numpy==1.26.4 scikit-learn==1.3.0 matplotlib==3.8.3 \
    python-box==7.3.2 PyYAML==6.0.2 tqdm==4.66.2 ensure==1.0.4 joblib==1.3.2 \
    types-PyYAML==6.0.12.12 Flask==3.0.2 Flask-Cors==4.0.0

# Copy application code
COPY . .

# Finally install the package in editable mode if needed
RUN pip install -e .

CMD ["python3", "app.py"]
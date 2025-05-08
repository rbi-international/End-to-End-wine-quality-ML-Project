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

# Install Python packages separately with specific versions
COPY requirements.txt .

# Install packages one by one to isolate any issues
RUN pip install --upgrade pip wheel setuptools && \
    pip install notebook==7.0.6 && \
    pip install numpy==1.26.4 && \
    pip install PyYAML==6.0.2 tqdm==4.66.2 ensure==1.0.4 joblib==1.3.2 types-PyYAML==6.0.12.12 && \
    pip install Flask==3.0.2 Flask-Cors==4.0.0 && \
    pip install python-box==7.3.2 && \
    pip install scikit-learn==1.3.0 && \
    pip install matplotlib==3.8.3

# Copy the application code
COPY . .

# Finally install the package in development mode (if needed)
RUN pip install -e .

CMD ["python3", "app.py"]
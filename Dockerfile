FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install system build deps (kept minimal)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       curl \
       ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install (using Python 3.11 to prefer prebuilt wheels)
COPY requirements.txt ./
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy backend sources
COPY . /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

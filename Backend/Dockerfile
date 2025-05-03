# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install build tools + netcat (for Postgres readiness check)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev netcat && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend code
COPY . .

# Start the app only after Postgres is reachable
CMD ["bash", "-c", "until nc -z db 5432; do sleep 1; done && uvicorn app.main:app --host 0.0.0.0 --port 8000"]

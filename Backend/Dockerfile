FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Wait until Postgres says “ready”, run the SQL, then launch FastAPI
CMD bash -c "until pg_isready -h db -p 5432; do sleep 1; done && \
             psql $DATABASE_URL -f /app/db_init.sql && \
             uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

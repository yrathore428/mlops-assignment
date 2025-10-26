FROM python:3.10-slim

WORKDIR /app
COPY artifacts /app/artifacts
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY serve.py .

CMD ["python", "serve.py"]

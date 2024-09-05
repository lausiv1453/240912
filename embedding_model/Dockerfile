FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY packages /packages

RUN pip install --no-cache-dir --find-links /packages -r requirements.txt

COPY . .

CMD ["python", "app.py"]

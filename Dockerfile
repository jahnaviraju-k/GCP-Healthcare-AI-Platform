FROM python:3.9-slim

WORKDIR /app

COPY deploy/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "api/predict_api.py"]

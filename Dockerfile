# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "uvicorn", "app:FastAPIApplication.get_application", "--host=0.0.0.0"]

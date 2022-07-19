# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /app
ENV FLASK_APP run.py

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
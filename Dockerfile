FROM python:3.9

WORKDIR /code
ENV FLASK_APP=app.py
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD flask run -h 0.0.0.0 -p 80
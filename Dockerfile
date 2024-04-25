FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip


COPY . .

RUN pip install -r requirements.txt
RUN flask db upgrade

EXPOSE 8080

CMD [ "flask", "run" , "--host", "0.0.0.0", "--port", "8080"]
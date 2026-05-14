FROM python:3.10

WORKDIR /app

COPY . .
RUN apt update && apt install -y iputils-ping
RUN pip install flask
RUN pip install psutil
RUN pip install prometheus_client

CMD ["python3"  , "app.py"]

FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt
    

COPY . /app

RUN chmod +x entrypoint.sh

EXPOSE 80


CMD ["/app/entrypoint.sh"]
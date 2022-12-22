FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt
# chmod +x entrypoint.sh

EXPOSE 8000

CMD ["/opt/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
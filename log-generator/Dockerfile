FROM python:3.11-slim

WORKDIR /app

COPY log_emitter.py .
COPY template_log.json .

RUN mkdir logs

CMD ["python", "-u", "log_emitter.py"]


FROM python:3.10-slim-bullseye
LABEL maintainer="user@domain.com"
LABEL name="pnadora"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update \
    && apt-get install --no-install-recommends --assume-yes \
        tini \
        curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
COPY requirements/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip==22.1.2 \
    && pip install --no-cache-dir -r app/requirements.txt

USER nobody
COPY . /app

WORKDIR /app
EXPOSE 8000
ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "gunicorn", "src.pnadora.main:app", "--config", "gunicorn_config.py" ]

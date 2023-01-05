FROM python:3.10-alpine as build
RUN adduser -s /bin/sh -D -u 1000 powermeter powermeter \
    && apk --no-cache update \
    && apk --no-cache add \
        zlib-dev \
        gcc \
        musl-dev \
        libffi-dev
WORKDIR /home/powermeter/
COPY requirements ./requirements
RUN pip install -r ./requirements/base.txt


FROM build as release
RUN pip install -r ./requirements/production.txt
USER powermeter
COPY --chown=powermeter:powermeter ./app ./powermeter
WORKDIR /home/powermeter/powermeter
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM release as dev
WORKDIR /home/powermeter/powermeter
USER root
RUN pip install -r ../requirements/dev.txt
USER powermeter

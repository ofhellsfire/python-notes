FROM python:3.9.8-slim AS compile-image

# Create virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /myservice

# Copy files
COPY foo/bar ./foo/bar
COPY foo/baz ./foo/baz
COPY cux ./cux
COPY config /config

RUN pip install -r ./cux/requirements.txt


FROM python:3.9.8-slim AS build-image

ENV PYTHONBUFFERED 1

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-it.sh

COPY --from=compile-image /opt/venv /opt/venv
COPY --from=compile-image myservice myservice
COPY --from=compile-image /config /config

WORKDIR /myserivce
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH="/foo"

ENTRYPOINT ["python", "cux/serivce.py"]


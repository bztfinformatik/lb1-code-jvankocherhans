FROM --platform=$BUILDPLATFORM python:3.11-alpine AS builder

WORKDIR /code
COPY requirements.txt /code
RUN pip3 install PyMySQL && apk add gcc musl-dev mariadb-connector-c-dev mysql-client 
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

RUN pip3 install --only-binary :all: greenlet


EXPOSE 8001

CMD ["flask", "run"]

FROM builder AS dev-envs

RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF

COPY --from=gloursdocker/docker / /

CMD ["flask", "run"]

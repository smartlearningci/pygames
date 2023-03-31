FROM python:3.12-rc-bullseye
USER root
RUN apt-get -y update
RUN apt-get -y install -y --no-install-recommends git
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN useradd -s /bin/bash -m vscode


ENTRYPOINT ["sleep", "infinity"]



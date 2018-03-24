FROM python:3.6-alpine
LABEL maintainer adioevan@gmail.com

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONPATH /movie_graph/

RUN mkdir -p /movie_graph/ /storage/movie_graph/
WORKDIR /movie_graph/

# Install system dependencies
RUN apk upgrade && \
    apk --no-cache add curl netcat-openbsd

COPY . /movie_graph/

# Install pip libraries
RUN pip install \
        --disable-pip-version-check \
        --requirement /movie_graph/requirements.txt && \
    rm -rf /root/.cache

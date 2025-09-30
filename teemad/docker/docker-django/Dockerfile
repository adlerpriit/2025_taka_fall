FROM python:slim-trixie

WORKDIR /user/src/app

# Install system dependencies and clean up
RUN apt update && apt upgrade -y && \
    apt install -y fish procps && \
    rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
FROM python:slim-trixie

WORKDIR /workspace

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user, install system dependencies, add sudo rights and clean up
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt update && apt upgrade -y \
    && apt install -y fish procps sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

EXPOSE 8000

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME

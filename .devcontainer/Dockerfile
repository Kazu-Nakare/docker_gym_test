FROM python:3.9-slim

# ユーザ'vscode'を作成する
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt update \
    && groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && apt install -y locales \
    && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt update && apt install -y --no-install-recommends \
    curl \
    git \
    xvfb \
    x11vnc \
    icewm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV DISPLAY :0

# 以下 pip

RUN pip install -U pip setuptools
RUN pip install flake8 autopep8

RUN pip install \
    numpy==1.23 \
    matplotlib \
    dezero \
    gym==0.25.2 \
    gym[classic_control]
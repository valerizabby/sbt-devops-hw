FROM jenkins/jenkins:lts

USER root

# Установка Python и необходимых инструментов
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean

USER jenkins
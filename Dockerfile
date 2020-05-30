# Django
# Version: 2.0
FROM python:3-slim
# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    libffi-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    vim

# Project Files and Settings
ARG PROJECT=django
ARG PROJECT_DIR=/var/www/${PROJECT}

RUN mkdir -p $PROJECT_DIR
RUN mkdir -p $PROJECT_DIR/temperature_sensor
COPY temperature_sensor $PROJECT_DIR/temperature_sensor
WORKDIR $PROJECT_DIR/temperature_sensor
RUN pip install -r requirements.txt

# Server
STOPSIGNAL SIGINT
ENTRYPOINT ["sh"]
CMD ["entry-point.sh"]

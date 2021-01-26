FROM python:3.8

## Support for scipy: https://stackoverflow.com/questions/36000204/cant-install-scipy

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get install -y vim wget unzip \
    && apt-get clean

COPY requirements.txt /python_files/

RUN pip install --upgrade pip \
    && ls /python_files \
    && pip install -r /python_files/requirements.txt

VOLUME [ "/python_files" ]

WORKDIR /python_files

CMD tail -f /dev/null
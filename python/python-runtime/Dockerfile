FROM python:3

## Support for scipy: https://stackoverflow.com/questions/36000204/cant-install-scipy

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get install -y \
    gcc \
    build-essential \
    zlib1g-dev \
    wget \
    unzip \
    cmake \
    python3-dev \
    gfortran \
    libblas-dev \
    liblapack-dev \
    libatlas-base-dev \
    && apt-get clean

VOLUME [ "/python_files" ]

CMD tail -f /dev/null
FROM python:3.8-alpine

MAINTAINER Olivier TASSEL <https://github.com/otassel>

RUN apk update
RUN apk add musl-dev wget git build-base

# Numpy
RUN pip install cython
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip install numpy 

# TA-Lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
  tar -xvzf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib/ && \
  ./configure --prefix=/usr && \
  make && \
  make install
RUN git clone https://github.com/mrjbq7/ta-lib.git /ta-lib-py && cd ta-lib-py && python setup.py install

RUN apk del musl-dev wget git build-base
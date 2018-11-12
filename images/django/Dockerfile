FROM python:3.7
RUN mkdir /code
COPY requirements/ /code/
WORKDIR /code
RUN pip install -r base.txt
COPY . /code

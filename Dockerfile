FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# install requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy source files
ADD . /code/
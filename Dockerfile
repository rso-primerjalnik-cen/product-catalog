FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# install requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy source files
ADD . /code/

CMD ["uvicorn", "app.api:fastapi_app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]

FROM python:3.9.11-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Sets up custom packages to be installed
COPY ./setup.py /code/setup.py

RUN pip install .

# Copies everything
COPY . /code/

CMD ["uvicorn", "apps.apis.daily_metrics_api.main:app", "--reload", "--port", "8000"]
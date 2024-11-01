FROM python:3.12.7-slim

LABEL authors="atrya"

WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN pip install poetry && \
    poetry install --no-dev

EXPOSE 8000

COPY . /code

CMD ["poetry", "run", "uvicorn", "src.app.main:create_app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--factory"]
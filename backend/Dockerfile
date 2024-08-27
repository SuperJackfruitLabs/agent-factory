FROM python:3.12-slim

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock* ./alembic.ini /app/

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

RUN poetry lock --no-update

RUN poetry install --no-dev

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

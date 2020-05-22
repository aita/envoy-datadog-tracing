FROM python:3

WORKDIR /usr/src/app

COPY poetry.lock .
COPY pyproject.toml .
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction

COPY . .

CMD [ "ddtrace-run", "python", "app.py" ]
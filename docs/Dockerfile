FROM python:3.12-slim

WORKDIR /docs

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    adduser --disabled-password --no-create-home docuser

USER docuser

COPY . .

EXPOSE 8001

CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8001"]

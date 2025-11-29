# Use official Python image
FROM python:3.11-slim

# System deps for e.g. pillow or psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev gettext curl && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /PortfolioBackend

# Copy dependency files first for docker cache
# COPY pyproject.toml poetry.lock* /app/  # if using poetry
# OR if using requirements.txt:
COPY requirements.txt /PortfolioBackend/

# Install Python deps (choose one)
# If using requirements.txt:
RUN pip install --upgrade pip && pip install -r requirements.txt

# If using poetry, uncomment:
# RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev --no-interaction

# Copy project
COPY . /PortfolioBackend

# Create a non-root user for security
RUN useradd --create-home appuser
RUN chown -R appuser:appuser /PortfolioBackend
USER appuser

# Make a directory for logs/static
RUN mkdir -p /app/staticfiles

# Entrypoint and ports
EXPOSE 8000
COPY ./entrypoint.sh /PortfolioBackend/entrypoint.sh
RUN chmod +x /PortfolioBackend/entrypoint.sh

CMD ["/app/entrypoint.sh"]

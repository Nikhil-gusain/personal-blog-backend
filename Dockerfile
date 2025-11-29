# Use official Python image
FROM python:3.11-slim

# Install system dependencies needed for psycopg / psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-venv \
    python3-dev \
    libpq-dev \
    build-essential \
    gcc \
    curl \
    gettext \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /PortfolioBackend

# Copy dependency files separately for caching
COPY requirements.txt /PortfolioBackend/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /PortfolioBackend

# Entrypoint
COPY ./entrypoint.sh /PortfolioBackend/entrypoint.sh
RUN chmod +x /PortfolioBackend/entrypoint.sh

# Create non-root user for security
RUN useradd --create-home appuser
RUN chown -R appuser:appuser /PortfolioBackend
USER appuser

# Make a directory for logs/static under the appuser
RUN mkdir -p /PortfolioBackend/staticfiles

EXPOSE 8000

CMD ["/PortfolioBackend/entrypoint.sh"]


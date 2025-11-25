FROM python:3.12-slim

# install awscli
RUN pip install awscli

WORKDIR /app
COPY . /app

# copy entrypoint
# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

# install requirements
RUN pip install -r requirements.txt

# ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "PortfolioBackend.wsgi:application", "--bind", "0.0.0.0:8000"]

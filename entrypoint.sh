#!/usr/bin/env bash
set -e

# Fetch parameters from SSM and export as env vars
export DATABASE_URL=$(aws ssm get-parameter \
  --name "/portfolio/dburi" \
  --with-decryption \
  --query "Parameter.Value" \
  --output text)

# optional: echo variable names only (not values) to logs for debugging
echo "Loaded SSM params: DATABASE_URL"

# Start Django (gunicorn, uvicorn, etc.)
exec "$@"

#!/usr/bin/env bash
set -e

# Set AWS region if not already set
export AWS_REGION=${AWS_REGION:-ap-south-1}

# Fetch parameter from SSM
export DATABASE_URL=$(aws ssm get-parameter \
  --name "/portfolio/dburi" \
  --query "Parameter.Value" \
  --output text)

echo "Loaded SSM params: DATABASE_URL=$DATABASE_URL"

# Run passed command
exec "$@"

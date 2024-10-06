#!/bin/bash

. .env

set -euo pipefail

# --env-vars-file .env doesnt work: it wants a YAML!!!

gcloud --project "$PROJECT_ID" run deploy \
    php-amarcord \
    --source . \
    --set-env-vars DB_PASS="$DB_PASS" \
    --set-env-vars DB_USER="$DB_USER" \
    --set-env-vars DB_HOST="$DB_HOST" \
    --set-env-vars DB_NAME="$DB_NAME" \
    --region europe-west8 \
    --allow-unauthenticated

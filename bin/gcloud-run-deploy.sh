#!/bin/bash

. .env

set -euo pipefail

# --env-vars-file .env doesnt work: it wants a YAML!!!

#    --set-env-vars PORT="80" \
# ERROR: (gcloud.run.deploy) spec.template.spec.containers[0].env: The following reserved env names were provided: PORT. These values are automatically set by the system.

gcloud --project "$PROJECT_ID" run deploy \
    php-amarcord-bin \
    --source . \
    --port 80 \
    --set-secrets DB_PASS="" \
#    --set-env-vars DB_PASS="$DB_PASS" \
    --set-env-vars DB_USER="$DB_USER" \
    --set-env-vars DB_HOST="$DB_HOST" \
    --set-env-vars DB_NAME="$DB_NAME" \
    --set-env-vars APP_NAME="$APP_NAME" \
    --set-env-vars APP_VERSION="$APP_VERSION" \
    --region europe-west8 \
    --allow-unauthenticated

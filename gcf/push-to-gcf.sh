#!/bin/bash

set -euo pipefail

echo Sourcing .env..
# source ../.env ||  fatal 2

.  ~/git/app-mod-workshop-set-by-step/.env

echo "Pushing ☁️ f(x)☁ to 🪣 $GS_BUCKET, along with DB config.. (DB_PASS=$DB_PASS)"

# gcloud functions deploy FUNCTION_NAME --set-env-vars FOO=bar,BAZ=boo

echodo gcloud --project "$PROJECT_ID" functions deploy php_amarcord_generate_caption \
    --runtime python310 \
    --region "$GCP_REGION" \
    --trigger-event google.cloud.storage.object.v1.finalized \
    --trigger-resource "$BUCKET" \
    --set-env-vars "DB_HOST=$DB_HOST,DB_NAME=$DB_NAME,DB_PASS=$DB_PASS,DB_USER=$DB_USER" \
    --source . \
    --entry-point generate_caption \
    --gen2

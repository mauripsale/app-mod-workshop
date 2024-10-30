#!/bin/bash

set -euo pipefail

source ../.env ||  fatal 2

echo "Pushing ☁️ f(x)☁ to 🪣 $GS_BUCKET, along with DB config.. (DB_PASS=$DB_PASS)"

# gcloud functions deploy FUNCTION_NAME --set-env-vars FOO=bar,BAZ=boo

echodo gcloud --project "$PROJECT_ID" functions deploy php_amarcord_generate_caption \
    --runtime python310 \
    --region "$GCP_REGION" \
    --trigger-event google.cloud.storage.object.v1.finalized \
    --trigger-resource "$BUCKET" \
    --set-env-vars FOO=bar,BAZ=boo,DB_PASS="$DB_PASS" \
    --source . \
    --entry-point generate_caption \
    --gen2

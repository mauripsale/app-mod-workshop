#!/bin/bash

set -euo pipefail

source ../.env ||  fatal 2

echo "Pushing ☁️ f(x)☁ to 🪣 $GS_BUCKET"

echodo gcloud --project "$PROJECT_ID" functions deploy php_amarcord_generate_caption \
    --runtime python310 \
    --region "$GCP_REGION" \
    --trigger-event google.cloud.storage.object.v1.finalized \
    --trigger-resource "$BUCKET" \
    --source . \
    --entry-point generate_caption \
    --gen2

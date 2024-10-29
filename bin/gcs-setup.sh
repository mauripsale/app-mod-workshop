#!/bin/bash

set -euo pipefail

. .env

echo "Listing or Creating now bucket: $GS_BUCKET .."

gsutil ls "$GS_BUCKET/" ||
    gsutil mb -l "$GCP_REGION" -p "$PROJECT_ID" "$GS_BUCKET/"

gsutil cp ./uploads/*.png "$GS_BUCKET/originals/"

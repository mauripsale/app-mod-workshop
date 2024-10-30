#!/usr/bin/env python

from google.cloud import storage
from google.cloud import aiplatform
import base64

# Replace with your project ID
#PROJECT_ID = "your-project-id"
PROJECT_ID='ricc-demos-386214'
# Replace with your GCS bucket name
BUCKET_NAME = "your-bucket-name"
#BUCKET="${PROJECT_ID}-public-images"

def generate_caption(event, context):
    """
    Cloud Function triggered by a GCS event.
    Args:
        event (dict): The dictionary with data specific to this type of event.
        context (google.cloud.functions.Context): The context parameter contains
                                                event metadata such as event ID
                                                and timestamp.
    """

    # Get the file information from the event
    file_name = event['name']
    bucket_name = event['bucket']
    # not sure they exist!
    #file_size = event['size']
    #content_type = event['contentType']

    print(f"Bucket: {bucket_name}")
    print(f"Object path: {file_name}")
    #print(f"Size: {file_size} bytes")
    #print(f"Content type: {content_type}")

    # Download the image from GCS
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    image_bytes = blob.download_as_bytes()

    # Encode the image in base64
    base64_image = base64.b64encode(image_bytes).decode('utf-8')

    # Generate a caption using Gemini
    aiplatform.init(project=PROJECT_ID, location="us-central1")
    response = aiplatform.execute_model(
#        model="gemini-1.5-pro-001",  # Replace with the desired Gemini model
        model="gemini-1.5-pro",  # Replace with the desired Gemini model
        instances=[
            {
                "prompt": f"Generate a caption for this image: ",
                "images": [
                    {
                        "data": base64_image,
                        "mime_type": "image/jpeg"  # Replace with the actual MIME type
                    }
                ]
            }
        ]
    )

    # Extract the caption from the response
    caption = response.predictions[0]['candidates'][0]['content']

    # Print the caption (you can also store it or use it as needed)
    print(f"Generated caption: {caption}")

    # TODO upload to images DB as caption.

def flag_inappropriate():
    '''TODO(ricc): ask gemini if its inappropriuate and if so, flag it and update DB with TRUE'''
    pass

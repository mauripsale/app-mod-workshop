#!/usr/bin/env python

from google.cloud import storage
from google.cloud import aiplatform
import base64
import os

# Import the function you want to test
from main import *
# Assuming your code is in main.py

def test_gemini_describe_image_from_local_file():
    """Tests the gemini_describe_image function with a local image."""
    test_image_path = "test-images/cloud-run-deploy-flags.png"

    # Load the local image
    with open(test_image_path, "rb") as image_file:
        image_bytes = image_file.read()

    # Encode the image in base64
    base64_image = base64.b64encode(image_bytes).decode('utf-8')

    # Set the image prompt
    image_prompt = "Generate a caption for this image: "

    # Call the function
    caption = gemini_describe_image_from_local_file(base64_image, image_prompt)

    # Print or assert the caption
    print(f"Generated caption: {caption}")
    # assert "expected string" in caption  # Add assertions as needed


def test_gemini_describe_image_from_gcs_for_riccardo():
    gcs_url = 'gs://ricc-demos-386214-public-images/RiccardoInVienna.jpg'
    caption = gemini_describe_image_from_gcs(gcs_url)
    # Print or assert the caption
    print(f"Generated caption for {gcs_url}: {caption}")
    # assert it contains blue.
    # Assert OCR for "Larry & Sergey"

def test_gemini_describe_image_from_gcs_for_gcloud_command():
    gcs_url = 'gs://ricc-demos-386214-public-images/cloud-run-deploy-flags.png'
    caption = gemini_describe_image_from_gcs(gcs_url)
    # Print or assert the caption
    print(f"Generated caption for {gcs_url}: {caption}")
    # assert it contains blue.
    # Assert OCR for "Larry & Sergey"

def test_update_db_with_string():
    '''This is secret also test needs .env to help..'''
    db_pass = os.getenv('DB_PASS', None)
    if db_pass is None:
        print("DB_PASS is not set. I cant proceed. Rummage in your .env file.")
        return 42

    print(f"db_pass: {db_pass}")
    update_db_with_description("image_1", "This is a first Unit Test", db_pass)
    update_db_with_description("PXL_20241014_062548507.jpg", "This is a second Unit Test", db_pass)



if __name__ == "__main__":
    #test_gemini_describe_image_from_local_file()
    #test_gemini_describe_image_from_gcs_for_riccardo()
    #test_gemini_describe_image_from_gcs_for_gcloud_command()
    test_update_db_with_string()


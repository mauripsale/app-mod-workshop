#!/usr/bin/env python

from google.cloud import storage
from google.cloud import aiplatform
import base64

# Import the function you want to test
from main import gemini_describe_image  # Assuming your code is in main.py

def test_gemini_describe_image():
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
    caption = gemini_describe_image(base64_image, image_prompt)

    # Print or assert the caption
    print(f"Generated caption: {caption}")
    # assert "expected string" in caption  # Add assertions as needed

if __name__ == "__main__":
    test_gemini_describe_image()

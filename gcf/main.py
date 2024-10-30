#!/usr/bin/env python

'''Documentation:


* Vertex:
* AI Studio: https://ai.google.dev/gemini-api/docs/vision

v0.5 - DB integration seems to work.
v0.4 - finally it works! pushing and cleaning up
'''
GCF_VERSION = '0.5'


from google.cloud import storage
from google.cloud import aiplatform
#import base64

import vertexai
from vertexai.generative_models import GenerativeModel, Part
import os
import pymysql
import pymysql.cursors



# Replace with your project ID
#PROJECT_ID = "your-project-id"
PROJECT_ID='ricc-demos-386214'

DEFAULT_PROMPT = "Generate a caption for this image: "
#DEFAULT_PROMPT2 = "What is shown in this image?"

# def gemini_describe_image_from_local_file(base64_image, image_prompt=DEFAULT_PROMPT):
#     '''This is currently broken..'''
#     raise "TODO"

def gemini_describe_image_from_gcs(gcs_url, image_prompt=DEFAULT_PROMPT):
    '''This is currently broken..'''

    # Generate a caption using Gemini
    # TODO auto-detect project id
    aiplatform.init(project=PROJECT_ID, location="us-central1")
    model = GenerativeModel("gemini-1.5-pro")

    response = model.generate_content([
            Part.from_uri(
                gcs_url,
                mime_type="image/jpeg", # TODO remove or test with PNG..
            ),

            image_prompt,
        ])

    print(f"Gemini spoken: '''{response.text}''' in class today!" )

    # Extract the caption from the response
    return response.text

def update_db_with_description(image_filename, caption, db_pass , db_user='appmod-phpapp-user', db_host='34.154.154.222', db_name='image_catalog'):
    '''
    '''
    #print(f"update_db_with_description(): Updating DB for img='{image_filename}' with caption '..'. ConnString='{db_conn_string}'")
    # Transforms the image from gs://bucket/my/image.png into /uploads/image.png.
    # Thats because thats how the app does it. Dont ask me why we embed /uploads/ in the app :)

    image_db_filename = f"uploads/{image_filename}"

    conn = None

    try:
        print("update_db_with_description(): Connecting to DB...")
        # Connect to the database
        #import ipdb; ipdb.set_trace()

        conn = pymysql.connect(host=db_host,
                             user=db_user,
                             password=db_pass,
                             database=db_name,)
        print("update_db_with_description(): Now the cursor...")
        cursor = conn.cursor()
        print("update_db_with_description(): Now sql..")

        # SQL query to update the database (replace placeholders with actual table and column names)
        sql = 'UPDATE images SET description = %s WHERE filename = %s'
        val = (caption, image_db_filename)

        # Execute the query
        cursor.execute(sql, val)
        conn.commit()

        print(f"[GCFv{GCF_VERSION}] Database updated successfully")

    except Exception as e:
        print(f"[GCFv{GCF_VERSION}] Error updating database: {e}")

    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()


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

    print(f"[GCFv{GCF_VERSION}] Bucket: {bucket_name}")
    print(f"Object path: {file_name}")
    print(f"Multifaceted event: {event}")
    #print(f"Size: {file_size} bytes")
    #print(f"Content type: {content_type}")


    # Download the image from GCS
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    print(f"Blob: {blob}")
    public_url = blob.public_url
    print(f"Blob public URL: {public_url}")
    gcs_full_url = f"gs://{bucket_name}/{file_name}"
    print(f"[GCFv{GCF_VERSION}] GCS full URL: {gcs_full_url}")

    caption = gemini_describe_image_from_gcs(gcs_full_url)

    # Print the caption (you can also store it or use it as needed)
    print(f"[GCFv{GCF_VERSION}] Generated caption: {caption}")

    # TODO upload to images DB as caption.
    # **MySQL Update Functionality**

    # Construct the connection string (replace placeholders with your actual values)
    #conn_string = f"mysql+pymysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}@{os.environ['MYSQL_HOST']}:{os.environ['MYSQL_PORT']}/{os.environ['MYSQL_DATABASE']}"
    #conn_string = os.environ('DB_PYTHON_CONNECTION_STRING')
    db_pass = os.getenv('DB_PASS', None)
    if db_pass is None:
        print("DB_PASS is not set. I cant proceed. Please get your ENV back together!")
        return -1
    update_db_with_description(file_name, caption, db_pass)
    return True

# def flag_inappropriate():
#     '''TODO(ricc): ask gemini if its inappropriuate and if so, flag it and update DB with TRUE'''
#     pass

import json
import base64
import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Initialize S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Extract file details from the event
        bucket_name = event.get('bucket_name')
        file_name = event.get('file_name')
        file_content = event.get('file_content')  # Base64-encoded content

        # Ensure required inputs are provided
        if not bucket_name or not file_name or not file_content:
            raise ValueError("bucket_name, file_name, and file_content are required")

        # Decode the file content
        decoded_file = base64.b64decode(file_content)

        # Upload the file to S3
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=decoded_file)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'File {file_name} uploaded successfully to {bucket_name}'})
        }
    except (BotoCoreError, ClientError, ValueError) as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }

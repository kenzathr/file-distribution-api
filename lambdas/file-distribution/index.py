"""
File Distribution Lambda Function

This module provides AWS Lambda handler for generating presigned URLs
to download files from S3 bucket securely.

Features:
- Generate presigned URLs for S3 objects
- Secure URL expiration (1 hour)
- Error handling for missing files
- JSON response format
"""

import json
import boto3
import os
from datetime import datetime

# Initialize AWS S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    AWS Lambda handler for presigned URL generation.
    
    Args:
        event (dict): API Gateway event containing:
            - pathParameters.fileId: File name to generate URL for
        
        context (dict): Lambda context
    
    Returns:
        dict: HTTP response with status code and body
    """
    # Extract file ID from path parameters
    try:
        file_id = event['pathParameters']['fileId']
    except (KeyError, TypeError):
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing fileId in path parameters'})
        }                                                                                   
    

    # Define S3 bucket name (can be set as environment variable)
    bucket_name = os.environ.get('BUCKET_NAME')
    if not bucket_name:
    return {
        'statusCode': 500,
        'body': json.dumps({'error': 'BUCKET_NAME environment variable not set'})
    }
    # Generate presigned URL for the specified file
    try:
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': file_id},
            ExpiresIn=3600  # URL expires in 1 hour
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'url': presigned_url})
        }   
    except s3_client.exceptions.NoSuchKey:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'File not found'})
        }   
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    

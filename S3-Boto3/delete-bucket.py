#!/usr/bin/env python3.9
import boto3
s3 = boto3.client('s3')
BUCKET_NAME = "devinstotaltechnology"
response = s3.delete_bucket(
    Bucket = BUCKET_NAME
)
print(response)

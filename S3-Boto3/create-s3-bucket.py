#!/usr/bin/env python3.9
import boto3
s3 = boto3.resource('s3')
BUCKET_NAME = <INSERT_BUCKET_NAME>

bucket = s3.create_bucket(
    ACL = 'public-read',
    CreateBucketConfiguration = {  #will not work if you choose us-east-1, must not include
        'LocationConstraint': 'us-east-2'
        },
    Bucket = BUCKET_NAME
)
print(bucket)

#!/usr/bin/env python3.9
import boto3

client = boto3.client('ec2')
response = client.delete_vpc(
    VpcId="vpc-0bcec0383f0464c32"
)
print(response)
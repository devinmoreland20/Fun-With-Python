#!/usr/bin/env python3.9

import boto3
ec2=boto3.client('ec2')

response = ec2.describe_snapshots(
    SnapshotIds=['snap-07485d57de30a8ef2']
)
print(response)
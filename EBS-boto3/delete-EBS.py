#!/usr/bin/env python3.9

import boto3
ec2 = boto3.client('ec2')
# volumes = ec2.volumes.all() # If you want to list out all volumes
# print(volumes)

response = ec2.describe_volumes()
delvol = ec2.delete_volume(
    VolumeId='vol-0e2f90d869cb95bf9'
    )





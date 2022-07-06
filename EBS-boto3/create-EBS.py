#!/usr/bin/env python3.9
import boto3
ec2 = boto3.resource('ec2')
volume = ec2.create_volume(
    AvailabilityZone='us-east-1a',
    Size=8,
    VolumeType='gp2'
)
print(volume)
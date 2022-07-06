#!/usr/bin/env python3.9
# import boto3   #This will create a snapshot 

# client = boto3.client('ebs')

# response = client.start_snapshot(
#     VolumeSize=8,
#     ParentSnapshotId='snap-0913f296cfd260670'
# )
# print(response['SnapshotId'])
import boto3
ec2 = boto3.resource('ec2')
volume = ec2.create_volume(
    AvailabilityZone='us-east-1a',
    Size=8,
    VolumeType='gp2',
    SnapshotId='snap-0913f296cfd260670'  #You can delete this and it will create a volume from scratch for us. 
)
print(volume)
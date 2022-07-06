#!/usr/bin/env python3.9

import boto3
ec2 = boto3.client('ec2')

response = ec2.delete_snapshot(
    SnapshotId='snap-0913f296cfd260670'
)
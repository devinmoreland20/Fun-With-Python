#!/usr/bin/env python3.9
import boto3
vpc = boto3.resource('ec2')

response = vpc.create_vpc(
    CidrBlock='10.0.0.0/16',
    InstanceTenancy='default'
    )

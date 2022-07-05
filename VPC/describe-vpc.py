#!/usr/bin/env python3.9
import boto3
vpc = boto3.client('ec2')
response = vpc.describe_vpcs()

# no_of_vpc = response["Vpcs"]

# for vpc in no_of_vpc:
#     print(vpc["VpcId"])



vpicid = "vpc-0bcec0383f0464c32"
response = vpc.describe_vpcs(
    VpcIds = [vpicid]
)
print(response)



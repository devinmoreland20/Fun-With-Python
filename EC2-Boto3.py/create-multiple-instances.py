#!/usr/bin/env python3.9
import boto3

ec2 = boto3.resource('ec2')
no_of_instances = int(input("How many instances:" ))


    
instance = ec2.create_instances(
    ImageId="ami-0cff7528ff583bf9a",
    InstanceType='t2.micro',
    KeyName='Mac',
    MaxCount= no_of_instances,
    MinCount= no_of_instances
)
print(instance)



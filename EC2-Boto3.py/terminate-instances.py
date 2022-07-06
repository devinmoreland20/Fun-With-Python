#!/usr/bin/env python3.9
import boto3
ec2 = boto3.client('ec2')

x = ec2.describe_instances()

data=x["Reservations"]

list1 = []   #list to put the results form the for loop in 
for instances in data:
    instance = instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        list1.append(instance_id)

response = ec2.terminate_instances(
    InstanceIds=list1
)
print(response)




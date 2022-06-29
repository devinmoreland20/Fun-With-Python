#!/usr/bin/env python3.9

ec2 = int(input("How many EC2 instance do you want: "))
dept = str(input("What department do you work in? "))
#print(ec2)
def gen(ec2):
    for i in range(ec2):
        yield i
for i in gen(ec2):
    i = id(i)
    n = (dept + str(i))
    print(n)







 
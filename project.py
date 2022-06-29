#!/usr/bin/env python3.9
def instances():
    ec2 = int(input("How many EC2 instance do you want: ")) 
    dept = str(input("What department do you work in? "))
    dept = dept.lower()
    for name in ["marketing", "accounting", "finops"]:
        s = name
    if dept == s:  
        print("Below is your list:")   
    else:
        print("You should not be using this genrator")
        exit()

    def gen(ec2):
        for i in range(ec2):
            yield i
    
    for i in gen(ec2):
        i = id(i)
        n = (dept + str(i))
        print(n)

instances()









 
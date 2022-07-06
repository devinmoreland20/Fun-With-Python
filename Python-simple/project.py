#!/usr/bin/env python3.9
def instances():   #this creates our function
    ec2 = int(input("How many EC2 instance do you want: "))  #varible for how many instances we want
    dept = str(input("What department do you work in? "))#Variable for which dept we work in
    dept = dept.lower()   #Lowercases all input for dept so that case errors do not effect it
    for name in ["marketing", "accounting", "finops"]:   #For loop to make variable for the depts
        s = name
    if dept == s:  #For loop so that if they are not in the right dept the function ends
        print("Below is your list:")   
    else:
        print("You should not be using this genrator")
        exit()

    def gen(ec2): #generator that will create range of instances
        for i in range(ec2):
            yield i
    
    for i in gen(ec2):
        i = id(i) #assigns unique id to our instances
        n = (dept + str(i)) #adds dept to our id
        print(n)

instances() #Starts the function









 
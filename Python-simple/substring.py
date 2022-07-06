def count_substring(string, sub_string):
    c=0  #this is our counter
    l=len(sub_string)   #This will be the length of the substring
    for i in range(len(string)):  #A for loop allows the code to be executed for set amount of time
        s=string[i:i+l] #String to iterate through the first string
        if s==sub_string: #s must be equal to substring or cdc in this ex. 
            c+=1 #for each cdc in string we will add 1 to our counter
    return c  #this will return the counter c
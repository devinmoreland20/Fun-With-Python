name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you today? "))

#print(name, end=" ")  #print function will by defualt add a new line after this. You fix this with the , end=" "
#print("is " + str(age) + " years old", end=" ")
#print("and loves the color " + color + ".") #this will not promtp a new line on out put so we removed the end= func. 

print(name, 'is', age, 'years old and lovers the color', color + '.', sep=" ")

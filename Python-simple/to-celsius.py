#!/user/bin/env python3.9

fahrenheit = float(input("What temperature in (in Fahrenheit) would you like converted to Celsius? "))
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "F is", round(celsius, 2), "C")
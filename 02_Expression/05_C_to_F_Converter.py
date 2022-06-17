"""
Exercise 5: Write a program which prompts the user for a Celsius temperature, 
convert the temperature to Fahrenheit, and print out the converted temperature.

To convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.

"""
inputc = float(input("Input Celcius Degree: "))
cnvt = inputc * 1.8 + 32
print(cnvt," Fahrenheit")

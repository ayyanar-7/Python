#Get Fahrenheit
F=float(input("Enter Fahrenheit value : "))

#Covert Celsius
C=(5/9.0)*(F-32)

#Display Output
print() #Empty line
print("{:.2f} Fahrenheit is {:.2f} Celsius".format(F,C))

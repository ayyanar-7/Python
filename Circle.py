#import math Library
import math

#Get Area of the Circle
A=float(input("Enter Area of the Circle : "))

#Calculate Radius and Circumference
R=math.sqrt(A*(7/22.0))
C=2*(22/7.0)*R

#Display Output
print("The information of given Area of Circle")
print("---------------------------------------")
print("Area of the Circle          : %9.2f"%A)
print("Radius of the Circle        : %9.2f"%R)
print("Circumference of the Circle : %9.2f"%C)

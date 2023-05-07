#Get Principal
P=float(input("Enter Principal amount : "))
#Rate of Interest
R=float(input("Enter Rate of Interest : "))
#No of Years
N=float(input("Enter number of Years : "))


#Do Calculation
CI=P*(1+(R/100))**N

#Display Output
print()
print("Compound Interest = {:.2f}".format(CI))
#Get Principal amount
P=float(input("Enter a Principal amount : "))
#Get number of Years
N=float(input("Enter number of Years : "))
#Get Rate of Interest
R=float(input("Enter the Rate of Interest : "))

#Do Calculation
SI=(P*N*R)/100

#Display Output
print("Principal amount = {:.2f} Rate of Interest = {:.2f} Number of Years = {:.2f}".format(P,\
                                                                                            N,\
                                                                                            R))
print() #Empty line
print("Simple Interest = {:.2f}".format(SI))
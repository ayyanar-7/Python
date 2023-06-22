#Get input
a=int(input("Enter a number of A : "))
b=int(input("Enter a number of B : "))
c=int(input("Enter a number of C : "))

#Check condition & display output
if(a>b & a>c):
    print("A is Biggest number : %.2f"%a)
elif(b>c):
    print("B is Biggest number : %.2f"%b)
else:
    print("C is Biggest number : %.2f"%c)
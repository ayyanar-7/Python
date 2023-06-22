#Get input
hours=int(input("Enter number of hours worked : "))
Rhours=hours
Othours=0

#Check Overtime
if(Rhours>40):
    Othours=Rhours-40;
    Rhours=40

#Do Calculation
Rwage=Rhours*150
Otwage=Othours*(150*1.5)

#Display output
print("Regular wage  : %13.2f"%Rwage)
if(Othours>0):
    print("Overtime wage : %13.2f"%Otwage)
    print("-----------------------------")
    print("Total wage    : %13.2f"%(Rwage+Otwage))
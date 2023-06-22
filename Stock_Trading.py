#Get input
X=int(input("Enter no of shares : "))
Y=float(input("Enter Each share purchase value : "))
Z=float(input("Enter Each share sold value : "))

#Do calculations
Pvalue=X*Y
Commission=Pvalue*(2/100.0)
Svalue=X*Z
Bro_commission=Svalue*(2/100.0)
Nrevenue=(Svalue-Bro_commission)-(Pvalue+Commission)

#Display result
print("---------------------------------------")
print("             STOCK TRADING             ")
print("---------------------------------------")
print("Purchase value       : %16.2f"%Pvalue)
print("Purchase commission  : %16.2f"%Commission)
print("Sales value          : %16.2f"%Svalue)
print("Brokerage commission : %16.2f"%Bro_commission)
print("Net Revenue          : %16.2f"%Nrevenue)


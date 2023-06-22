#Get Sales turnover
sales=float(input("Enter Sales Turnover : "))

#Calculate Commission
if(sales<5000):
    commission=sales*(5/100.0)
elif(sales<10000):
    commission = sales * (5 / 100.0)
elif(sales<20000):
    commission = sales * (5 / 100.0)
elif(sales<25000):
    commission = sales * (5 / 100.0)
else:
    commission = sales * (5 / 100.0)

#Display commission
print("Commission : %.2f"%commission)

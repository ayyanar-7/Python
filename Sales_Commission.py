
while(True):
    # Get sales turnover
    sales = float(input("Enter a sales turnover amount : "))

    #Calculate commission
    Com=sales*12.5

    #Display commission
    print("Commission : %10.2f"%Com)

    #Check condition
    opt=input("Calculate another (y/n)? ")
    if(opt=='y'):
        continue
    else:
        break






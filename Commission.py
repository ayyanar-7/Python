def com(x):
    if(x<10000):
        return 10.0
    elif(x<20000):
        return 15.0
    else:
        return 20.0


x=int(input("Enter a sales amount : "))
print(x*com(x)/100)


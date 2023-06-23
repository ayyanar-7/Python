while(True):
    a = int(input("Enter a numbers :"))
    b = int(input())

    print("sum = %d"%(a+b))
    print()

    opt=input(("Do you want to continue? (y/n) : "))
    if(opt=='y'):
        continue
    else:
        break

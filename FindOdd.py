def Odd(x):
    list=[]
    for i in range (1,x+1,2):
        list.append(i)
    return list


x=int(input("Enter a number : "))
print(Odd(x))

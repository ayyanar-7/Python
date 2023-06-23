#Find Prime or not
def prime(x):
    for i in range(2,x//2):
        if(x%i==0):
            return False
    return True


#Get input
x=int(input("Enter a number : "))

res=prime(x)

#Display result
if(res):
    print("Given number is Prime number")
else:
    print("Given number is not a Prime number")
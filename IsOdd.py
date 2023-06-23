def IsOdd(n):
    if(n%2==1):
        return True
    else:
        return False


n=int(input("Enter a number : "))
s=IsOdd(n)
if(s):
    print("Given number is Odd number")
else:
    print("Given number is Even number")
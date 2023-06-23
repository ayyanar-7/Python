def Welcome():
    print("Welcome to python programming!")
    n=int(input("Enter a number : "))
    return n
n=Welcome()
if(n%2==0):
    print("Given number is Even")
else:
    print("Given number is Odd")
#Find feet and inches
def FeetAndInch(x):
    feet=x//12
    inch=x-feet*12

    return feet,inch

#Display tuple
x=int(input("Enter total length of inches : "))
print(FeetAndInch(x))
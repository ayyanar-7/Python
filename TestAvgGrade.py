#Calculate average mark
def avg(tamil,english,maths,science,social):
    average = (tamil+english+maths+science+social)/5.0

    return average

#Calculate grade
def grade(mark):
    if(mark>=90 and mark<=100):
        return 'A'
    elif(mark>=80):
        return 'B'
    elif(mark>=70):
        return 'C'
    elif(mark>=60):
        return 'D'
    elif(mark<60 and mark>=0):
        return 'E'
    else:
        print("Invalid input")


#main program
tamil = float(input("Enter Tamil mark : "))
english = float(input("Enter English mark : "))
maths = float(input("Enter Maths mark : "))
science = float(input("Enter Science mark : "))
social = float(input("Enter Social Science mark : "))

print("Average mark = %.2f"%avg(tamil,english,maths,science,social))

print("------------------------------------------------------------")
print("                     Grading System                         ")
print("------------------------------------------------------------")

print("Tamil             : %c"%grade(tamil))
print("English           : %c"%grade(english))
print("Maths             : %c"%grade(maths))
print("Science           : %c"%grade(science))
print("Social Science    : %c"%grade(social))

#Get Marks
m1=int(input("Enter test 1 mark : "))
m2=int(input("Enter test 2 mark : "))
m3=int(input("Enter test 3 mark : "))

#DO calculation
Avg=(m1+m2+m3)/3

#Display output
print()
print("Average Mark : %.2f"%Avg)
if(Avg>90):
    print()
    print("Very good, Keep it up.")

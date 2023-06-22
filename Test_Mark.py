#Get 3 Test marks
M1=int(input("Enter Test-1 Mark : "))
M2=int(input("Enter Test-2 Mark : "))
M3=int(input("Enter Test-3 Mark : "))

#Calculate Total and Average
Total=M1+M2+M3
Avg=Total/3.0

#Display Output
print("Three test marks")
print("---------------------------------")
print("Test-1 mark : %19d"%M1)
print("Test-2 mark : %19d"%M2)
print("Test-3 mark : %19d"%M3)
print()
print("Total       : %19d"%Total)
print("Average     : %19.2f"%Avg)
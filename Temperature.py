#Get Temperature
t=float(input("Enter a Temperature in Celsius : "))

#Check Temperature & Display output
if(t<20):
    print("Cold outside")
elif(t<=25):
    print("Pleasant weather")
elif(t<=30):
    print("Warm weather")
else:
    print("Very hot outside")
#Display Heading
print("Kilometres per hour          Miles per hour")

#Diplay KPH to MPH
for i in range(60,111,10):
    print("{0:^18d}          {1:^14.3f}".format(i,i*0.6214))
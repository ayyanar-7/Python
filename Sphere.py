#Get Radius
R=float(input("Enter the Radius of the Sphere : "))

#Calculate Volume & Area
V=(4*(22/7.0)*(R**3))/3
A=4*(22/7.0)*R*R

#Display Output
print("Volume and Are of Sphere Calculator")
print("-----------------------------------")
print("Radius of the Sphere = {:12.2f}".format(R))
print("Volume of the Sphere = {:12.2f}".format(V))
print("Area of the Sphere   = {:12.2f}".format(A))
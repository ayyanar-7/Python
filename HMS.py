def HMS(s):
    h=(int)(s/3600)
    m=(int)((s-(h*3600))/60)
    s=(int)(s-((m*60)+(h*3600)))

    return h,m,s


x=int(input("Enter number of seconds to finish the work : "))
print(HMS(x))
while(True):
    #Get temperature
    T=int(input("Enter the Temperature : "))

    #Check temperature & Display message
    if(T<105):
        print("Reduce termostat")
    else:
        print("Temperature accept")
        break

def future_value():
    P = int(input("Present Value: "))
    i = float(input("Interest Rate: "))
    t = float(input("months: "))

    f = P*(1+i)**t

    print("The information for your account is: ")
    print("Present Value: $",P)
    print("Interest Rate: %",i)
    print("After 18 months, the value of your acount will be $", f)

future_value()
    

    
    
    


def print_average():
    a = float(input("Type a number: "))
    if a<0:
        print("Average was 0")
    else:
        n1 = a
        n2 = 1

        a = float(input("Type a number: "))

        while a>=0:
            n1 += a
            n2 += 1
            a = float(input("Type a number: "))

        print("Average was",(n1/n2))

print_average() 

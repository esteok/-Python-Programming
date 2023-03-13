def integers(a,b):
    sum=0
    for x in range (a,b+1):
        sum= sum + x
        print (x, end = " ")
    print("\n")
    return sum

print("sum of numbers: ", integers (5,10))

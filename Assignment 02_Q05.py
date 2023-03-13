import math

def find_area():
    x=int(input("Enter the length of the first rectangle: "))
    w1=int(input("Enter the width of the first rectangle "))
    y=int(input("Enter the length of the second rectangle: "))
    w2=int(input("Enter the width of the second rectangle "))
    a1=x*w1
    a2=y*w2
    print("Area A: ",a1)
    print("Area b: ",a2)

    if a1>a2:
        print("Area A is greater than Area B")
    elif a1<a2:
        print("Area B is greater than Area A")
    else:
        print("Area A is equal to Area B")

find_area()
    

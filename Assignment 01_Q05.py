import math

a=int(input("Enter count of A seats: "))
b=int(input("Enter count of B seats: "))
c=int(input("Enter count of C seats: "))

A= a*15
B= b*12
C= c*9
total = A + B + C

print("Income from class A seats: $", A)
print("Income from class B seats: $", B)
print("Income from class C seats: $", C)
print("Total income: $",total)

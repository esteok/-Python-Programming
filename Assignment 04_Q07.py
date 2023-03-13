import random

def dice_sum():
    sum=int(input("Desired dice sum : "))
    n1=random.randint(1,6)
    n2=random.randint(1,6)
    while n1+n2!= sum:
        n1=random.randint(1,6)
        n2=random.randint(1,6)
        print(n1,"and",n2,"=",(n1+n2))
        if((n1+n2)==sum):
            break

dice_sum()

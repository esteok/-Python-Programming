import random
num = 25

for i in range (0,3):
    x = random.randint (1, 150)
    y = x * num
    f = 0
    if x>=10 and x<20: f = float (y) * .2
    elif x >= 20 and x < 50:
        f = float (y) * .3
    elif x>= 50 and x < 100: f = float (y) * .4
    elif x>= 100:
        f = float (y) * .5

print("Number of Packages Purchased:", x)
print ("Discount Amount: $",f)
print ("Total Amount: $", y-f)

import random
even = 0
for i in range(0,100):
    a = random.randint(-100, 100)
    if (a % 2 ==0):
        even +=1
    

print("Out of 100 random numbers,",100-even,"were odd, and", even, "were even")

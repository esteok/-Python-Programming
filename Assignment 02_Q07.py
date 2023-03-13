def rep1(x, y):
    z = ""

    if(y <= 0):
            return z
    for i in range(y):
                z = z + x
    return z
 
x = input("Enter a string: ")
y = int(input("Enter amount of repititions: "))

print(x, " ->", rep1(x, y))



x = input("Enter a string: ")
y={}
for i in x:
    if i in y:
        y[i]=y[i]+1
    else:
        y[i] = 1
a = max(y, key = y.get)
print("The character that appears most frequently in the string is",a.upper())

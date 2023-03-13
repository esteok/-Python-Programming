import math

a = int(input('Enter Number: '))
b = float(input('Enter Number: '))
c = float(input('Enter Number: '))
d = float(input('Enter Number: '))
e = float(input('Enter Number: '))
f = float(input('Enter Number: '))
g = float(input('Enter Number: '))
h = float(input('Enter Number: '))
i = float(input('Enter Number: '))
j = float(input('Enter Number: '))

list1 = [a, b, c, d, e, f, g, h, i, j]

total = sum (list1)
low = list1[0]
high = list1[9]
for k in range(1,len(list1)) :
    if list1[k] < low:
         low = list1[k]
    elif list1[k] > high:
         high = list1[k]
average = sum(list1) / 10

print("Low: ",low)
print("High: ",high)
print("Total: ",total)
print("Average: ",average)


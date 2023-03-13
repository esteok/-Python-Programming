START = 1
END = 8
print("first nested loop")
print()
#first nested loop
for i in range(START, END):
    for j in range(START, i+1):
        print('*', end='')
    print()

print()
print("second nested loop")
print()

#second nested loop
for i in range(END - 1, 0, -1):
    for j in range(START, i+1):
        print('*', end='')
    print()
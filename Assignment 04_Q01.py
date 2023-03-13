import random

file = input ("Enter the name of the file to which result should be written: ")
x = int (input("Enter the number of random numbers to be written to the file: "))
myList = open(file,'w')
for i in range(x):
               myList.write(str(random.randint(1,100)) + "\n")
myList.close()

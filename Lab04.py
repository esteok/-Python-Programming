import math
firstNum = int(input("enter an odd number "))
secondNum = int(input("enter another number "))

def printAllNum(a,b):
    print ("print all numbers: ")
    for x in range (a,b +1 ):
        print (x, end = " ")

printAllNum(firstNum,secondNum)

def printOddNum(a,b):

    print("\nprint all odd numbers:")
    for x in range(a, b, 2):
        print (x, end = " ")
printOddNum(firstNum,secondNum)

def printEvenSum(a,b):
    print("\nprint all of odd Numbers:")
    sumValue = 0
    for i in range(firstNum, secondNum+1):
        if i%2!=0:
            sumValue += i
        print(sumValue)

def printOddSquare(a,b):
    print("print sum of the square of the odd Numbers:")
    sumValue = 0
    for i in range(firstNum, secondNum+1):
        if i%2!=0:
            sumValue += i**2
    print(sumValue)

printOddSquare(firstNum,secondNum)


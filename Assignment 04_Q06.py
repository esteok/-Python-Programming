while True:
    number1 = float(input("Enter a number : "))
    number2 = float(input("Enter another number : "))

    print("The sum of the numbers you entered is",(number1+number2))

    a= input("do you want to do that again? (y/n): ")
    if a == "y":
        continue
    if a == "n":
        break


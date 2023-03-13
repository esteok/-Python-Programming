x = int(input("Enter the number of days: "))

print("Day","\t","Pennies")
print("---------------------------")
    
def forLoop(x):
    penniesEarned = 0.01
    for i in range(1,x + 1):
        print(i,"\t","$", penniesEarned)
        penniesEarned = penniesEarned*2
    total = penniesEarned-0.01
    print("The total salary for", x, "days is: $", total)


forLoop(x)

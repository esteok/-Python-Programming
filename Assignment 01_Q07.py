wallSize = int(input("Enter wall space in square feet: "))
price = float(input("Enter paint price per gallon: "))
numOfGallons = wallSize / 115
numOfHours = numOfGallons * 8.00
costOfPaint = price * numOfGallons
laborCharge = numOfHours * 20.00
totalCost = costOfPaint + laborCharge

print("Gallons of paint: ",numOfGallons)
print("Hours of labor: ",numOfHours)
print("Paint charges: $",costOfPaint)
print("Labor charges: $",laborCharge)
print("Total cost: $",totalCost)

def getCountySaleTax(sales):
    return sales*.02

def getStateSaleTax(sales):
    return sales*.04

sales=float(input("Enter the total sales for the month: "))

countyTax=getCountySaleTax(sales)
stateTax=getStateSaleTax(sales)

print("Monthly sales $", sales)
print("State tax $", stateTax)
print("County tax $",countyTax)
print("Total tax = $",countyTax+stateTax)

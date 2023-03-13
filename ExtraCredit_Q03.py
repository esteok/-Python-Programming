file = open("WorldSeries.txt", "r")

dict1 = {}
dict2 = {}
year = 1903

for line in file.readlines():
    line = line.strip()
    dict1[year] = line
    if dict2.__contains__(line):
        dict2[line] += 1
    else:
        dict2[line] = 1
    year = year + 1
file.close()

while 1:
    year = int(input("Enter a year in the range 1903-2020: "))
    if year < 1903 or year > 2020:
        print("The data for the year " + str(year) + " is not included in our database")
    elif year == 1904 or year == 1994:
        print("The world series wasn't player in the year " + str(year))
    else:
        print("The team that won the world series in " + str(year) + " is the " + dict1[year])
        print("They won the world series " + str(dict2[dict1[year]]) +" times")

    ch = str(input("Do you want continue, type 'y' for yes, 'n' for No "))
    while ch != "y" and ch != "n":
        ch = str(input("Do you want continue, type 'y' for yes, 'n' for No "))
    if ch != "y":
        break

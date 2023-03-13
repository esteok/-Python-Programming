file = open("riskfactors.csv", "r")

indicator = []
dict = {}
i = 0
for line in file.readlines():
    i = i + 1
    if i >= 6:
        data = line.strip().split(",")
        data[11] = data[11].replace("%","")
        data[13] = data[13].replace("%","")
        if i == 6:
            indicator.append(data[0])
            indicator.append(data[1])
            indicator.append(data[5])
            indicator.append(data[7])
            indicator.append(data[11])
            indicator.append(data[13])
            dict[indicator[0]] = []
            dict[indicator[1]] = []
            dict[indicator[2]] = []
            dict[indicator[3]] = []
            dict[indicator[4]] = []
            dict[indicator[5]] = []
        else:
            dict[indicator[0]].append(data[0])
            dict[indicator[1]].append(float(data[1]))
            dict[indicator[2]].append(float(data[5]))
            dict[indicator[3]].append(float(data[7]))
            dict[indicator[4]].append(float(data[11]))
            dict[indicator[5]].append(float(data[13]))
file.close()

file = open("best_and_worst.txt", "w")
file.write("{:<31}: {:<30}  {:}\n".format("Indicator","Min", "Max"))
file.write("---------------------------------------------------------------------------------------\n")
for i in range(1, 6):
    list = dict[indicator[i]]
    max = 0
    min = 0
    for j in range(len(list)):
        if list[max] < list[j]:
            max = j
        elif list[min] > list[j]:
            min = j
    file.write("{:<31}: {:<20} {:>6}     {:<15} {:>6}\n".format(
        indicator[i], dict[indicator[0]][min], round(dict[indicator[i]][min],1), dict[indicator[0]][max], round(dict[indicator[i]][max],1)))

file.close()

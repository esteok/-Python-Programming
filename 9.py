# function which reads and stores data in the two-dimensional array and returns that data
MONTH_IN_YEAR = 12
def getData():
      data=[]
      print("Enter highest temperature for each month of year : ")
      for i in range(MONTH_IN_YEAR):
            high = input()
            high=int(high)
            data.append([high])
      print("Enter lowest temperature for each month of year : ")
      for i in range(MONTH_IN_YEAR):
            low = input()
            low=int(low)
            data[i].append(low)
      # returning data
      return data    

# function which returns average high temperature for the year
def averageHigh(data):
      sum=0
      for i in range(MONTH_IN_YEAR):
            sum += data[i][0]
      
      return sum / MONTH_IN_YEAR

# function which returns the average low temperature for the year
def averageLow(data):
    sum=0
    for i in range(MONTH_IN_YEAR):
        sum += data[i][1]
      
    return sum / MONTH_IN_YEAR

# function which returns the index of highest high temperature
def highTemp(data):
      highest=data[0][0]
      index = 0
      for i in range(MONTH_IN_YEAR):
            if data[i][0] > highest:
                  highest = data[i][0]
                  index = i
      return index

# function which returns the index of lowest low temperature
def lowTemp(data):
      lowest = data[0][1]
      index = 0
      for i in range(MONTH_IN_YEAR):
            if data[i][1]<lowest:
                  lowest=data[i][1]
                  index = i
      return index


if __name__ == '__main__':
    data=getData()
      
    print("List of highest and lowest temperatures for each month of year")
    for i in range(MONTH_IN_YEAR):
        print(data[i][0], end=" ")
    print()
    for i in range(MONTH_IN_YEAR):
        print(data[i][1], end=" ")
    print()
    print("Average high temperature for the year : ",round(averageHigh(data),2))
    print("Average low temperature for the year : ",round(averageLow(data),2))
    print("highest high temperature for the year : ",data[highTemp(data)][0])
    print("lowest low temperature for the year : ",data[lowTemp(data)][1])

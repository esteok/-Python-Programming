my2dList = [[-2,3,-5], [-8,4,-6], [9,-3,77],  [11,-2,9]]

def count_odd(my2dList):
    odd_values = {}
    print("2D list")
    for row in my2dList:
        print(row)
        
        for i in range(len(row)):
            col = row[i]
            if i not in odd_values.keys():
                odd_values[i] = 0
            if col % 2 == 1 and col < 0:
                odd_values[i] = 1 + odd_values[i]
    
    print("\n\nNumber of odd negative values ")
    for k, v in odd_values.items():
        print("Col",k + 1, ":", v)


count_odd(my2dList)

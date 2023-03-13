import math

def euclidean(p1, p2):
    sum = 0 
    # loop to iterate over points
    for i in range(len(p1)):
        diff = (p1[i] - p2[i]) ** 2 
        sum = sum + diff 

    e_dist = math.sqrt(sum)
    
    # return distance
    return e_dist
      
def main():
    two_d_list = []
    with open('data.txt') as file:
        for points in file.readlines():
            x,y = points.strip().split(",")
            two_d_list.append([int(x),int(y)])
            
    count = 0
    for i in range(len(two_d_list)):
        count += 1
        # print header
        print("{:>8}{:>1}".format("P", count), end="")
        
    count = 0
    
    for p1 in two_d_list:
        count += 1
        print("{:1}{:<1}".format("P", count), end="")
        for p2 in two_d_list:
            print(p1[0], p2[0])
            

    # count = 0    
    
    # # nested loops to iterate over each sublist  
    # for sublist1 in list_of_lists:
        
    #     # convert sublist to point
    #     point1 = np.array(sublist1)
        
    #     # increase count by 1
    #     count += 1
        
    #     # display verticle header
    #     print("{:1}{:<1}".format("P", count), end="")
        
    #     # for each sublist, iterate again all sublists 
    #     for sublist2 in list_of_lists:
            
    #         # convert sublist to point
    #         point2 = np.array(sublist2)
            
    #         # now, make a function call to find the euclidian distance between two points
    #         dist = euclidD(point1, point2)
            
    #         # display distance
    #         print("{:>9.2f}".format(dist), end="")
        
    #     print()

# program starts from here
if __name__ == "__main__":
    
    # calling main()    
    main()
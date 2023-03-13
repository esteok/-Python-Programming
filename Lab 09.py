import random
k=random.randint(2,10)
list1 = []
print("Enter",k,"values:")
for i in range(k):
    x=(int(input("Enter value "+str(i+1)+": ")))
    list1.append(x)
    
def collapse(list1):
    myList=[]
    for i in range(0,len(list1),2):
        if(i==len(list1)-1):
            x=list1[i]
        else:
            x=list1[i]+list1[i+1]
        myList.append(x)
    return myList

list2=collapse(list1)
print("Old list:",list1)
print("Collapse List:",list2)


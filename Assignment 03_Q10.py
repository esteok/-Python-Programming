my_dict = {'a':15, 'c':35, 'b':10}
keys = list(my_dict.keys())
values = list(my_dict.values())
print("Keys: ",keys,)
print("Values: ",values)
print("Key-Value pairs")

for x,y in my_dict.items():
    print(x,y)

print("\n")

print ("Key-Value pairs- sorted by key")
keys.sort()
for k in keys:
    print(k,my_dict[k])

print("\n")

print("Key-Value pairs-sorted by Values")
List=[]
for x,y in my_dict.items():
    List.append([y,x])
List.sort()
for i in List:
    print(i[1],i[0])

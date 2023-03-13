def remove_duplicates(sortedlist):
    my_list = []
    for i in sortedlist:
        if my_list == [] or my_list[-1] != i:
            my_list.append(i)
    return my_list

def myFunc():
    sortedlist = ['be', 'be','is', 'not', 'or', 'question', 'that', 'the', 'to', 'to']
    print("original list:", sortedlist)
    print("list after removing duplicates:", remove_duplicates(sortedlist))

myFunc()

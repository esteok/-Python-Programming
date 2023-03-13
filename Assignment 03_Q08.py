list = ['how', 'are', 'you?']
def double_list(list):
    double=[]
    for i in list:
        double.append(i)
        double.append(i)
    return double

print('original list: ', list)
print('double list: ', double_list(list))

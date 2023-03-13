def histogram():
    x=input("Enter a string: ")
    a = list(set(x))
    a.sort()
    count = 0
    for i in a:
        if i!= " " :
            count=x.count(i)
            print(str(i).upper(), end = " ")
            print(count*"* ")

histogram()

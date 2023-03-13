import random
def three_heads():
    string = []
    while len(string) < 3 or string[-3:] != [0, 0, 0]:
        string1 = random.randint(0, 1)
        string.append(string1)
        if string1 == 0:
            print('H', end=' ')
        else:
            print('T', end=' ')
    print("\nThree heads in a row!")

three_heads()

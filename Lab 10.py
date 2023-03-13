Dictionary1 = {'Janet': 87, 'Logan': 62, 'Whitaker': 46, 'Alyssa': 100, 'Stef': 80, 'Jeff': 88, 'Kim': 52, 
'Sylvia': 95}
Dictionary2 = {'Logan': 62, 'Kim': 52, 'Whitaker': 52, 'Jeff': 88, 'Stef': 80, 'Brian': 60, 'Lisa': 83,
 'Sylvia': 87}

def dictionaryFunction(Dictionary1,Dictionary2):
    resultDictionary = {}
    for i in Dictionary1:
        for x in Dictionary2:
            if i==x:
                if Dictionary1[i]==Dictionary2[x]:
                    resultDictionary[i] = Dictionary1[i]

    return resultDictionary

print(dictionaryFunction(Dictionary1,Dictionary2))

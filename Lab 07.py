user=input("Enter a string ")

def get_consonant():
    string = user.upper()
    print("Old string: ",string)
    count=0
    list1 = ("B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z")
    
    for i in string:
        if i in list1:
            count = count+1
            sentence = string.replace("B", "*").replace("R","*").replace("N","*").replace("T","*").replace("T"," ").replace("E"," ")

    print("New String: ",sentence)
    print("Number of consonant characters: ",count)

get_consonant()

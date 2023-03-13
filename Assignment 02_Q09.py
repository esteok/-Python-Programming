txt=input("Enter a string: ")
s=txt.lower()
list1=('a','e','i','o','u')
count=0
count2=0

def vowels(count):
    for x in s:
        if x in list1:
            count=count+1
    return count


def consonants(count2):
    for x in s:
        if x not in list1:
            count2=count2+1
    return count2


print ("The string you entered includes" , vowels(count), "vowels and", consonants(count2), "consonants")







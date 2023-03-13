def threeRail(plainText):
    cipherText = ""
    for i in range(2,-1,-1):
        for j in range(i, len(plainText), 3):
            cipherText = cipherText + plainText[j]
    return cipherText


plainText = "ABCDEFGHI"
cipherText = threeRail(plainText)

print("PlainText: " + plainText)
print("CipherText: " + cipherText)

print()

plainText = "JACK IN THE BOX"
cipherText = threeRail(plainText)

print("PlainText: " + plainText)
print("CipherText: " + cipherText)

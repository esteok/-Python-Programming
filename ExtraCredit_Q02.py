def substitutionDecrypt(cipherText,key):
    abc = "abcdefghijklmnopqrstuvwxyz "
    cipherText = cipherText.lower()
    plainText = ""
    for i in cipherText:
        x = key.find(i)
        plainText = plainText + abc[x]
    return plainText


testKey1 = "zyxwvutsrqponmlkjihgfedcba "
cipherText = "gsv jfrxp yildm ulc"

print("CipherText: " + cipherText)
print("PlainText:", substitutionDecrypt(cipherText, testKey1))

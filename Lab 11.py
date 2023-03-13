f=open("numbers.txt", "r")
lines = f.readlines()

negativeCount = 0
oddCount =0
positiveCount = 0
positiveSum = 0
negativeSum = 0

for i in lines:
    s=i.rstrip ()
    a,x=s.split(" ")
    x=int(x)
    if x%2==1:
        oddCount+=1
    if x<0:
        negativeCount+=1
        negativeSum+=x
    else:
        positiveCount+=1
        positiveSum+=x



print("negative count =", negativeCount)
print("odd Count=", oddCount)
print("negative sum=",negativeSum)
print("positive average=", (positiveSum/positiveCount))

f.close()

f1 = open("thisFile.txt","r")
f2 = open("thatFile.txt","w")
lines = f1.readlines()
f1.close()
iter = 0
for line in lines:
    if iter % 2 == 0:
        f2.write(line)
    iter = iter + 1

f1.close()
f2.close()






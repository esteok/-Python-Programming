import string

file=input("enter file name ")
file=open(file,"r")
f=file.read()
f=f.lower()
count={}

file.close()

for i in string.ascii_lowercase:
    count[i]=0
for i in f:
    if i in count:
          count[i]=count[i]+1

print("letter\tcount")

for i in count.keys():
          print("{0}\t{1}".format(i,count[i]))




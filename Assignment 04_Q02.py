def conversion():
   for f in range(-10,11):
       c=(f-32)*(5/9)
       file.write("{0:<12.2f}{1:.2f}\n".format(f,c))

file=open("tempconv.txt","w")
file.write("{0:12s}{1:12s}\n".format("Fahrenheit","Celsius"))       
conversion()  

file.close()

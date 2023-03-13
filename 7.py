rows=4 
cols=3 
alpha=[] 
for i in range(rows):
    alpha.append([0]*cols)
    
print("part a")

for i in range(rows):
    print(alpha[i]) 
for i in range(rows):
    if i==0:
        alpha[i]=[1]*cols 
    else:
        alpha[i]=[3]*cols 
        
print("part b")
for i in range(rows):
    print(alpha[i]) 
    
for i in range(rows):
    alpha[i][0]=2 
    for i in range(rows):
        alpha[i][1]=alpha[i][0]*2 
        alpha[i][2]=alpha[i][1]*2 
        
print("part c")
for i in range(rows):
    print(alpha[i]) 
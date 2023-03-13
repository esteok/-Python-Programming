num=30
num_series=0.0

for x in range(1, 31):
    num_series=num_series+float(x/num)  
    num=num-1

print(num_series)

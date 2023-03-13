years = int(input('Enter the number of years '))
months = 12
total_sum = 0.0

for i in range(years):
    sum= 0.0
    print('\nFor year ', i + 1)
    for month in range(months):
        rain = float(input(f'Enter the rainfall amount for the month {month + 1}: '))
        sum += rain
    total_sum += sum 

total_months = years * months
average = total_sum / total_months
print("For months: ", total_months)

print('Total rainfall: ', format(total_sum, '.2f'),' inches')  
print('Average monthly rainfall: ', format(average, '.2f'), 'inches')

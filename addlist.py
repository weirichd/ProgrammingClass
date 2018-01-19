number = ''

num_list = []
# Keep looping until they enter 0
while number != 0:
    number = float(input('Please input a number '))
    
    num_list.append(number)

# Print out their numbers:
for number in num_list:
    print(number)


# Find the total
total = 0
for number in num_list:
    total = total + number

print('The total = {}'.format(total))
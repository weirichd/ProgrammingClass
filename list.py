# List program by David Weirich

# Let the user input a list of items, then print it out


# Step 1: Let the user input their list

my_items = []

done = False

while not done:
    next_item = input('Please input an item (Q to quit): ')
    
    if next_item == 'Q':
        done = True
    else:
        my_items.append(next_item)

# Step 2: Print out the list

for item in my_items:
    print('My item is ' + item)
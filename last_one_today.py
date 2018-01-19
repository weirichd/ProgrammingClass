done = False

my_items = []

while not done:
    item = input('Please type an item (Q to quit) ')
    
    if item == 'Q':
        done = True
    else:
        my_items.append(item)
        

def count_cheese(l): 
    count_ch = 0
    count_bt = 0
    for item in l:
        if item == 'cheese':
            count_ch = count_ch + 1
        if item == 'boots':
            count_bt = count_bt + 1
            
    
    return count_ch, count_bt

cheese_ammount, boots_ammount = count_cheese(my_items)

print("You said cheese {} times. You said boots {} times".format(cheese_ammount, boots_ammount))
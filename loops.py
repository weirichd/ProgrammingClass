name = ''

while name != 'Q':
    name = input('What is your name? (Enter Q to quit) ')
    if name == 'David':
        print("You're the best.")
    elif name == 'Paul':
        print("Go away.")
    elif name != 'Q':
        print('Hey there, {}.'.format(name))
    else:
        print('Goodbye.')

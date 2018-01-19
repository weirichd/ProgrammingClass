# My first function
def greet(person):
    print('Good morning, ' + person + '.')
    
def jump(person, height = 4, unit = 'inches'):
    if height <= 4:
        print(person + ' jumped {} {} in the air!'.format(height, unit))
    else:
        print(person + ' did not jump {} {} in the air.'.format(height, unit))

# Let's use the function
# greet('David')
# greet('Adam')
# greet('Cesley')

#jump('Mr. Bowman', 3, 'centimeters')
#jump('Keff', 4)
#jump('David', 100, 'feet')
#jump('Adam', unit = 'miles')
#jump(unit = 'feet', height = 8, person = 'Roy')
#jump(person = 'ben', unit = 'miles', height = 5)


def math_stuff(x, y):
    sum = x + y
    product = x * y
    difference = x - y
    
    return sum, product, difference

s, p, d = math_stuff(7, 3)

print('S = {}. P = {}. D = {}.'.format(s, p, d))

david = {
    'First' : 'David',
    'Last' : 'Weirich',
    'Job' : 'Data Scientist',
    'Favorite Food' : 'Waffles',
    'Hometown' : 'Petoskey, MI',
    'Favorite Colors' : ['grey']
    }

def tell_about(person):
    print('Let me tell you about ' + person['First'] + ' ' + person['Last'] + ',')
    print('from ' + person['Hometown'] + '.')
    print('They are a ' + person['Job'] + '.')
    print('Also, they love ' + person['Favorite Food'] + '.')
  #  print('Favorite color is {}'.format(person['Favorite Colors']))    

    for color in person['Favorite Colors']:
        print('They like the color ' + color + '.')
    
    print()
    
lydia_a = {
    'First' : 'Lydia',
    'Last' : 'Agee',
    'Job' : 'Unemployed currently',
    'Favorite Food' : 'Grilled Cheese',
    'Hometown' : 'Cheboygan, MI',
    'Favorite Colors' : ['blue', 'pink', 'green']
}

keff = {
    'First' : 'Keff',
    'Last' : 'Beckett',
    'Job' : '7th grade student',
    'Favorite Food' : 'Subway',
    'Hometown' : 'Lincoln, NE',
    'Favorite Colors' : ['black', 'teal']
}
    
people_list = [david, lydia_a, keff]
    
for person in people_list:
    tell_about(person)
number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))

opp = input('What operation? ')

if opp == '+':
    answer = number1 + number2
elif opp == '-':
    answer = number1 - number2
elif opp == '*':
    answer = number1 * number2
elif opp == '/':
    answer = number1 / number2
else:
    print("Sorry, {} is not understood.".format(opp))
    exit()

message = '{} {} {} = {}'.format(number1, opp, number2, answer)

print(message)
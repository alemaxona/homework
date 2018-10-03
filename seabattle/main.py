__author__ = 'alemaxona'

''' 
main.py - Game logic
'''


from models import Field, Gamer


print('\n+++SEABATTLE+++')
print('\nEnter field size:')


# Select field size
while True:
    try:
        field_x = int(input('X = '))
        if int(field_x) < 3:
            print('Enter number > 3!')
        #elif int(x) > 10:
            #print('Enter number < 10 !')
        else:
            break
    except ValueError:
        print('Enter number please!')

while True:
    try:
        field_y = int(input('Y = '))
        if int(field_y) <= 0:
            print('Enter number > 0!')
        #elif int(y) > 10:
            #print('Enter number < 10 !')
        else:
            break
    except ValueError:
        print('Enter number please!')

# Init player 1
input_player1 = input('\nEnter name player1: ')
print('Welcome player', input_player1)

player1 = Gamer(input_player1)

# Init player 2
input_player2 = input('\nEnter name player2: ')
if input_player1 == input_player2:
    input_player2 += '.1'
    print('Welcome player', input_player2)

player2 = Gamer(input_player2)

# Show field
field = Field(field_x, field_y)
field.init_field()
print('\n FIELD')
for i in field.size:
    print(i)

# Enter coordinates ship
print(player1.name, '\nEnter coordinates ship (1 cell)')
player1_coo_one = input('X = ')
player1_coo_one = input('Y = ')


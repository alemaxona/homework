__author__ = 'alemaxona'


from random import shuffle


while True:
    def split_list(user_list, size):
        new_list = []
        while len(user_list) >= size:
            pre_list = user_list[:size]
            new_list.append(pre_list)
            user_list = user_list[size:]
        return new_list


    def move_position_cell(user_value):
        if user_value == 'w':
            if position_cell[0] >= 1:
                field[position_cell[0]][position_cell[1]] = field[position_cell[0] - 1][position_cell[1]]
                field[position_cell[0] - 1][position_cell[1]] = '[]'
                return [position_cell[0] - 1, position_cell[1]]
            else:
                print('You have gone beyond the field. Repeat input.\n')
                return [position_cell[0], position_cell[1]]
        elif user_value == 's':
            if position_cell[0] >= 0:
                field[position_cell[0]][position_cell[1]] = field[position_cell[0] + 1][position_cell[1]]
                field[position_cell[0] + 1][position_cell[1]] = '[]'
                return [position_cell[0] + 1, position_cell[1]]
            else:
                print('You have gone beyond the field. Repeat input.\n')
                return [position_cell[0], position_cell[1]]
        elif user_value == 'a':
            if position_cell[1] >= 1:
                field[position_cell[0]][position_cell[1]] = field[position_cell[0]][position_cell[1] - 1]
                field[position_cell[0]][position_cell[1] - 1] = '[]'
                return [position_cell[0], position_cell[1] - 1]
            else:
                print('You have gone beyond the field. Repeat input.\n')
                return [position_cell[0], position_cell[1]]
        else:
            if position_cell[1] >= 0:
                field[position_cell[0]][position_cell[1]] = field[position_cell[0]][position_cell[1] + 1]
                field[position_cell[0]][position_cell[1] + 1] = '[]'
                return [position_cell[0], position_cell[1] + 1]
            else:
                print('You have gone beyond the field. Repeat input.\n')
                return [position_cell[0], position_cell[1]]


    result_array = [x for x in range(1, 17)]
    result_array = split_list(result_array, 4)
    result_array[-1][-1] = '[]'

    array = [x for x in range(1, 17)]
    shuffle(array)
    field = split_list(array, 4)
    field[-1][-1] = '[]'

    position_cell = [3, 3]

    print('\n*** 15 ***\n')
    while field != result_array:
        for row in field:
            print(row)
        try:
            user_input = input('\nPress keys w,s,a,d to move []: ')
            if user_input.lower() != 'w' and \
                    user_input.lower() != 's' and \
                    user_input.lower() != 'a' and \
                    user_input.lower() != 'd':
                print('Press keys only w,s,a,d!\n')
                continue
            else:
                position_cell = move_position_cell(user_input)
        except IndexError:
            print('You have gone beyond the field. Repeat input.\n')
        except KeyboardInterrupt:
            print('Ok, bye!')
            break
        except EOFError:
            print('Ok, bye!')
            break

    if field != result_array:
        break
    else:
        print('Yeah!')
        user_input = input('\nDo you wont new game? (Y/N) ')
        if user_input.lower() == 'y':
            continue
        else:
            print('Ok, bye!')
            break

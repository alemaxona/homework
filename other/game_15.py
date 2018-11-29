__author__ = 'alemaxona'

from random import shuffle


def split_list(user_list, size):
    new_list = []
    while len(user_list) >= size:
        pre_list = user_list[:size]
        new_list.append(pre_list)
        user_list = user_list[size:]
    return new_list


result_array = [x for x in range(1, 17)]
result_array = split_list(result_array, 4)
result_array[-1][-1] = '[]'
print(result_array)

array = [x for x in range(1, 17)]
shuffle(array)
field = split_list(array, 4)
field[-1][-1] = '[]'


print('*** 15 ***\n')
while field != result_array:
    input('\nPress keys w,s,a,d to move []\n')
    for i in field:
        print(i)


__author__ = 'alemaxona'


from random import randint


def gen_int():
    '''Generator random integer'''
    while True:
        yield randint(1, 1000)


x = gen_int()
print(x)
print(next(x))
print(next(x))


# x = range(1, 10, 3)
# print(tuple(x))
# print(list(x))


def range_2(x, y, z=1):
    '''Generator like type range'''
    while x < y:
        if z == 1:
            yield x
            x += 1
        else:
            yield x
            x = x + z


x_2 = range_2(1, 10)
print(x_2)
print(list(x_2))

x_2 = range_2(1, 10, 3)
print(x_2)
print(tuple(x_2))

x_2 = range_2(1, 10, 4)
print(x_2)
print(list(x_2))

x_2 = range_2(1, 10, 5)
print(x_2)
print(list(x_2))


# l = ['1', '2', '3']
# x = map(int, l)
# print(x)
# print(tuple(x))


def map_2(func, value):
    '''Generator like map()'''
    for element in value:
        x = func(element)
        yield x


l_2 = ['1', '2', '3']
x_2 = map_2(int, l_2)
print(tuple(x_2))
x_2 = map_2(int, l_2)
print(list(x_2))


# a = [10, 20, 30, 40]
# print(list(enumerate(a)))


def enumerate_2(value):
    '''Generator like enumerate()'''
    index = 0
    while index < len(value):
        rez = (index, value[index])
        yield rez
        index += 1


a = [10, 20, 30, 40]
print(list(enumerate_2(a)))


# a = [10, 20, 30, 40]
# b = ('a', 'b', 'c', 'd', 'e')
# print(list(zip(a, b)))


def zip_2(value1, value2):
    '''Generator like zip()'''
    if len(value1) > len(value2):
        index = 0
        while index < len(value2):
            rez = (value1[index],value2[index])
            yield rez
            index += 1
    else:
        index = 0
        while index < len(value1):
            rez = (value1[index], value2[index])
            yield rez
            index += 1


a = [10, 20, 30, 40]
b = ('a', 'b', 'c', 'd', 'e')
print(list(zip_2(a, b)))

a = [10, 20, 30, 40, 50, 60, 70]
b = ('a', 'b', 'c', 'd', 'e')
print(list(zip_2(a, b)))
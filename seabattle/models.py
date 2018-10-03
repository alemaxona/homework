__author__ = 'alemaxona'

'''
 models.py - Classes objects game
'''


class Storage(object):
    player = None
    ship = []
    shot = []

    @staticmethod
    def add_player(value):
        Storage.player = value

    @staticmethod
    def add_ship(value):
        Storage.ship.append(value)

    @staticmethod
    def add_shot(value):
        Storage.shot.append(value)


class Gamer(object):

    ''' Gamers in game only two! '''

    queue = 0

    def __init__(self, name):
        self.name = name
        Gamer.queue += 1


class Field(object):

    ''' Field game '''

    def __init__(self, size, size2):
        self.size = size
        self.size2 = size2
        self.mark = '*'

    def init_field(self):
        self.size = [list(i) * int(self.size) for i in self.mark] * int(self.size2)
        return self.size


class Ship(object):
    def __init__(self, size):
        self.size = size


class Shot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


'''
s = Storage
s.add_shot([2,3])
s.add_shot([3,3])
print(s.shot)

s1 = Storage
print(s1.shot)
'''
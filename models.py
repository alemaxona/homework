# -*- coding: utf-8 -*-

__author__ = 'sobolevn'

from utils import get_input_function


class Storage(object):  # storage = Storage()
    obj = None

    items = None

    done = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
            cls.done = None
        return cls.obj


class BaseItem(object):
    def __init__(self, heading, done=''):
        self.heading = heading
        self.done = done

    def __repr__(self):
        return self.__class__

    @classmethod
    def construct(cls):
        raise NotImplemented()


class ToDoItem(BaseItem):
    def __str__(self):
        return 'ToDo: {}{}'.format(
            self.heading,
            self.done,
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        done = ' -'
        return ToDoItem(heading, done)


class ToBuyItem(BaseItem):
    def __init__(self, heading, price, done=''):
        super(ToBuyItem, self).__init__(heading)
        self.price = price
        self.done = done

    def __str__(self):
        return 'ToBuy: {} for {}{}'.format(
            self.heading,
            self.price,
            self.done,
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        price = input_function('Input price: ')
        done = ' -'
        return ToBuyItem(heading, price, done)


class ToReadItem(BaseItem):
    def __init__(self, heading, url, done=''):
        super(ToReadItem, self).__init__(heading)
        self.url = url
        self.done = done

    def __str__(self):
        return 'ToRead: {} for {}{}'.format(
            self.heading,
            self.url,
            self.done
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        url = input_function('Input URL: ')
        done = ' -'
        return ToReadItem(heading, url, done)
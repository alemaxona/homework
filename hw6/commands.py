# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import inspect
import json

# import custom_exceptions
from custom_exceptions import UserExitException
from models import BaseItem, Storage
from utils import get_input_function

__author__ = 'sobolevn'


class BaseCommand(object):
    @staticmethod
    def label():
        raise NotImplemented()

    def perform(self, objects, *args, **kwargs):
        raise NotImplemented()


class ListCommand(BaseCommand):
    @staticmethod
    def label():
        return 'list'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))


class DoneCommand(BaseCommand):
    @staticmethod
    def label():
        return 'done'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        print('Select item type:')
        i = 0
        for index, obj in enumerate(objects):
            if str(obj.done) == ' -':
                i += 1
                print('{}: {}'.format(index, str(obj)))

        if i == 0:
            print('All items is done')
            return

        input_function = get_input_function()
        selection = None

        while True:
            try:
                selection = int(input_function('Input number: '))
                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')

        for index, obj in enumerate(objects):
            if selection == index:
                obj.done = ' +'
                print('Item is done!')


class UnDoneCommand(BaseCommand):
    @staticmethod
    def label():
        return 'undone'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        print('Select item type:')
        i = 0
        for index, obj in enumerate(objects):
            if str(obj.done) == ' +':
                i += 1
                print('{}: {}'.format(index, str(obj)))

        if i == 0:
            print('All items is undone!')
            return

        input_function = get_input_function()
        selection = None

        while True:
            try:
                selection = int(input_function('Input number: '))
                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')

        for index, obj in enumerate(objects):
            if selection == index:
                obj.done = ' -'
                print('Item is undone!')


class NewCommand(BaseCommand):
    @staticmethod
    def label():
        return 'new'

    @staticmethod
    def _load_item_classes():
        # Dynamic load:
        # def class_filter(klass):
        #     return inspect.isclass(klass) \
        #            and klass.__module__ == BaseItem.__module__ \
        #            and issubclass(klass, BaseItem) \
        #            and klass is not BaseItem

        # classes = inspect.getmembers(
        #         sys.modules[BaseItem.__module__],
        #         class_filter,
        # )
        # return dict(classes)

        from models import ToDoItem, ToBuyItem, ToReadItem

        return {
            'ToDoItem': ToDoItem,
            'ToBuyItem': ToBuyItem,
            'ToReadItem': ToReadItem,
        }

    def perform(self, objects, *args, **kwargs):
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{}: {}'.format(index, name))

        input_function = get_input_function()
        selection = None
        selected_key = None

        while True:
            try:
                selection = int(input_function('Input number: '))
                selected_key = list(classes.keys())[selection]

                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')

        selected_class = classes[selected_key]
        print('Selected: {}'.format(selected_class.__name__))
        print()

        new_object = selected_class.construct()

        objects.append(new_object)
        print('Added {}'.format(str(new_object)))
        print()
        return new_object


class ExitCommand(BaseCommand):
    @staticmethod
    def label():
        return 'exit'

    def perform(self, objects, *args, **kwargs):
        raise UserExitException('See you next time!')

# -*- coding: utf-8 -*-
__author__ = 'alemaxona'


# Упражнения

# +1. Дан класс:
#     class Lock(object):
#       def __init__(self):
#         self.lock = False
    
#     Сделать менеджер контекста, который может переопределить 
#     значение lock на True внутри блока контекста.


# +2. Сделать менеджер контекста, который бы проглатывал все исключения вызванные 
#    в теле и писал их в консоль, пример использования:
    
#     with no_exceptions():
#       1 / 0 # => logs: ZeroDivisionError

#     print('Done!') # => continues execution


# +3. Сделать менеджер контекста, который бы мог измерять время выполнения блока кода, 
#    пример использования:
    
#     with TimeIt() as t:
#       some_long_function()

#     print('Execution time was:', t.time)


# 1
class Lock:
    def __init__(self):
        self.lock = False

    def __enter__(self):
        self.lock = True
        return  self.lock

    def __exit__(self, *args):
        self.lock = False
        print('Exit, Again False.')


with Lock() as f:
    print(f)


# 2
class Exten:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __enter__(self):
        try:
            rez = self.value1 / self. value2
            return rez
        except Exception as f:
            return 'Exception message:', f
    
    def __exit__ (self, *args):
        print('Continues execution')

with Exten(4, 2) as f:
    print(f)
with Exten(1, 'str') as f:
    print(f)
with Exten(1, '0') as f:
    print(f)


# 3
from datetime import datetime

class Code_time:
    def __init__(self):
        pass

    def __enter__(self):
        a = datetime.now()
        print((2 ** 2048) ** 1024)
        b = datetime.now()
        rez = b.second - a.second
        return rez

    def __exit__(self, *args):
        pass


with Code_time() as f:
    print('Run time is {} seconds.'.format(f))


# Практическое задание:

# +1. Пользователь по GET запросу на адрес / получает
# сообщение: "Число загадано"

# +2. Пользователь по POST запросе на адрес /guess
# получает один из следующих результатов: ">", "<", "="

# +3. Если число угадано - загадываем новое число

# +4. Flask при старте сервера - устанавливает seed для
# random, генерирует случайное число для угадывания

# +5. Администратор задает seed для модуля рандом через
# переменную окружения FLASK_RANDOM_SEED

# О чем подумать?
# + Все пользователи угадывают одно число или
# каждый свое?

# + Можно ли считать количество попыток и количество угаданных чисел?

# + Как хранить данные между запросами?


from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, validators
import random


app = Flask(__name__)
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'Very hard secret key'
)


class ContactForm(FlaskForm):
    number = IntegerField(label='number', validators=[
        validators.DataRequired()
    ])
    

random.seed(1)


def get_secret_number():
    global secret_number
    secret_number = random.randint(1, 20)
    return secret_number


@app.route('/', methods=['GET'])
def set():
    try:
        if request.method == 'GET':
            get_secret_number()
            print('secret number is', secret_number)
            return 'Guess the number!'
    except Exception:
        return 'Only GET requests.'


@app.route('/guess', methods = ['POST'])
def guess():
    try:
        if request.method == 'POST':
            print('form number is', request.form['number'], 'type', type(request.form['number']))
            if int(request.form['number']) > secret_number:
                return '<'
            elif int(request.form['number']) < secret_number:
                return '>'
            elif int(request.form['number']) == secret_number:
                get_secret_number()
                return 'Gud job! Guess the new number!'

    except Exception:
        return 'Number not setted, needed GET request.'


if __name__ == '__main__':
    app.run()

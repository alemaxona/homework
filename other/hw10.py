# -*- coding: utf-8 -*-
__author__ = 'alemaxona'


from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators
import json


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='My secret key',
    WTF_CSRF_ENABLED=False,
)


class FormHw(FlaskForm):
    email = StringField(validators=[
        validators.length(min=6, max=32),
        validators.email(),
        validators.DataRequired()
    ])

    password = StringField(validators=[
        validators.length(min=6, max=32)
    ])


@app.route('/locales')
def view_locales():
    data = {'locales': ['ru', 'en', 'it']}
    print(data)
    convert_data = json.dumps(data)  # Преобразует словарь в строку
    return convert_data


@app.route('/sum/<int:num1>/<int:num2>')  # <int: - тип данных
def usr_sum2(num1, num2):
    rez = int(num1) + int(num2)
    return 'sum: ' + str(rez)


@app.route('/greet/<user_name>')
def home(user_name):
    return 'hello: ' + user_name


@app.route('/form/user', methods=['GET', 'POST'])
def auth():
    data = {'status': '0', 'error': []}
    data = json.dumps(data)
    data_f = {'status': '1', 'error': 'Mail Error'}
    data_f = json.dumps(data_f)
    form = FormHw(request.form)
    if request.method == 'POST':
        if form.validate():
            return data
        else:
            return data_f
    if request.method == 'GET':
        return 'JSON world!'


@app.route('/serve/<path:path>')
def usr_path(path):
    file = '/Users/alemaxona/Documents/Projects/venv/lern12flask/' + path
    print(file)
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError:
        return '404'


if __name__ == '__main__':
    app.run()

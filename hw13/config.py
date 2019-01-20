from os import urandom

key = urandom(15)

class Configuration:
    DEBUG = True
    SECRET_KEY = key
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/alemaxona/Documents/Projects/venv/db_flask/db_flask.db'
from os import urandom

key = urandom(15)
# path_db = r'sqlite:///C:/sqlite/db_flask.db'  # win


class Configuration:
    DEBUG = True
    SECRET_KEY = key
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = path_db
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/alemaxona/Documents/Projects/venv/db_flask/db_flask.db'  # mac

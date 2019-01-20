from datetime import date
from main import db


class Book(db.Model):
    __tablename__ = 'Book'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(10), nullable=True)
    text = db.Column(db.String(100), nullable=False)
    deleted = db.Column(db.Boolean, default=True)
    data_create = db.Column(db.Date, default=date.today)

    def __repr__(self):
        return 'Author: {}'.format(self.author)

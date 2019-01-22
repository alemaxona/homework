from flask import Flask, request
from config import Configuration
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if Book.query.count() == 0:
            return 'No data'
        else:
            book = Book.query.all()
            results = []
            for b in book:
                author = b.author
                post = b.text
                date = b.data_create
                results.append([author, post, date])
            return str(results)
    else:
        return 'Enter Get request.'

@app.route('/create', methods=['GET', 'POST'])
def insert_db():

    from models import Book
    from forms import PostForm

    if request.method == 'POST':
        form = PostForm(request.form)
        if form.validate():
                post = Book(**form.data)
                db.session.add(post)
                db.session.commit()
                return 'POST created!'
        else:
            return 'Form not valid.'  
    else:
        return 'Enter POST request.'


if __name__ == "__main__":
    from models import *

    db.create_all()
    app.run()

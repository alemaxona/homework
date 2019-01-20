
from wtforms_alchemy import ModelForm
from models import Book


class PostForm(ModelForm):
    class Meta:
        model = Book
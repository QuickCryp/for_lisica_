from django import forms

from .models import Genre


class BookFilterForm(forms.Form):
    genre_choices = [('', 'Выберите жанр')] + list(Genre.objects.values_list('name', 'name').distinct()) # получаем все жанры(их name)
    genre = forms.ChoiceField(choices=genre_choices, required=False) # выводим в качестве поля в шаблон
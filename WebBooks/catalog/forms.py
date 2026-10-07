from datetime import date
from django import forms
from django.forms import ModelForm
from .models import Author
from .models import Book



class AuthorsForm(forms.Form):
    first_name = forms.CharField(label="Имя автора")
    last_name = forms.CharField(label="Фамилия автора")
    date_of_birth = forms.DateField(label="Дата рождения",
                                     initial=date.today(),
                                     widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_of_death = forms.DateField(label="Дата смерти",
                                     initial=date.today(),
                                     widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class BooksForm(forms.Form):
    model = Book
    fields = ['title', 'genre', 'language', 'author', 'summary','isbn']
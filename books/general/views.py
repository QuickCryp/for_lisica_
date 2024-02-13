from django.shortcuts import render
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Book, Genre
from .forms import BookFilterForm


def home(request): 
    search_query = request.GET.get('search', '') # получаем данные из поля search
    if search_query: # если поле содержит нужные нам имя | описание  то выводим
        books = Book.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    else:
        books = Book.objects.all()

    filter_form = BookFilterForm(request.GET) # получаем нашу форму
    if filter_form.is_valid(): # если форма для поиска по жанру заполнена, то ищем жанр
        genre = filter_form.cleaned_data.get('genre')
        if genre:
            books = books.filter(genre__name=genre)  # Используем двойное подчеркивание для доступа к полю name в связанной модели Genre

    context = { # контекст в шаблон
        'books': books,
        'filter_form': filter_form
    }
    template = 'pages/index.html'

    return render(request, template, context) # рендерим страницу


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        'book': book
    }
    template = 'pages/detail.html'

    return render(request, template, context)


class CreateBookView(CreateView):
    model = Book # указываем модель для создания
    fields = ['name', 'genre', 'description', 'author'] # указываем поля для формы
    template_name = 'pages/create.html'
    success_url = reverse_lazy('home:home') # редирект в успешном случае

    def form_valid(self, form): # если форма валидная, то сохраняем
        response = super().form_valid(form)
        return response


class CreateGenreView(CreateView):
    model = Genre
    fields = ['name']
    template_name = 'pages/create.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("home:home")
    template_name = 'pages/delete.html'
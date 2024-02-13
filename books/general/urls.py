from django.urls import path

from .views import home, book_detail, CreateBookView, CreateGenreView,  BookDeleteView


app_name = 'home'
urlpatterns = [
    path('', home, name='home'), # путь для домашней страницы
    path('detail/<int:book_id>/', book_detail, name='detail_book'), # путь для детальной страницы каждой книги
    path('create/', CreateBookView.as_view(), name='create'), # путь для создания книги
    path('genre-create/', CreateGenreView.as_view(), name='genre-create'), # путь для создания жанра
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete') # путь для удаления книги
]
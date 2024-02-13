from django.contrib import admin

from .models import Book, Genre


class BookAdmin(admin.ModelAdmin):
    model = Book
    fields = ['name', 'genre', 'description', 'author']
    search_fields = [
        'name', 'author', 'genre'
    ]


class GenreAdmin(admin.ModelAdmin):
    model = Genre
    fields = ['name']
    search_fields = ['name']


admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
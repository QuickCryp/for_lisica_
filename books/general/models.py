from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=256) # имя жанра

    def __str__(self) -> str: # строковое представление в административной панели
        return self.name
    
    class Meta: # Meta классы. Для административной панели
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class Book(models.Model):
    name = models.CharField(max_length=256) # имя книги
    author = models.CharField(max_length=128) # автор книги
    description = models.TextField() # описания книги
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT) # жанр книги, уникальный ключ для жанра

    def __str__(self) -> str: # строковое представление в административной панели
        return self.name
    
    class Meta: # Meta классы. Для административной панели
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
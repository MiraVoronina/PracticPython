from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Админ-класс для модели Author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    search_fields = ('first_name', 'last_name')  # Возможность поиска по имени и фамилии

admin.site.register(Author, AuthorAdmin)

# Админ-класс для модели Genre
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Показываем только название жанра
    search_fields = ('name',)  # Возможность поиска по имени жанра

admin.site.register(Genre, GenreAdmin)

# Админ-класс для модели Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')  # Показываем название, автора и жанры книги
    search_fields = ('title',)  # Возможность поиска по названию книги
    list_filter = ('author', 'genre')  # Добавляем фильтрацию по автору и жанру

    def display_genre(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()])  # Отображаем все жанры книги
    display_genre.short_description = 'Genres'  # Заголовок для колонки с жанрами

admin.site.register(Book, BookAdmin)

# Админ-класс для модели BookInstance
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')  # Показываем книгу, статус, дату возврата и id
    list_filter = ('status', 'due_back')  # Добавляем фильтрацию по статусу и дате возврата

admin.site.register(BookInstance, BookInstanceAdmin)

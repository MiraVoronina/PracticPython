from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('books/', views.book_list, name='book-list'),  # Перечень книг
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # Детальная информация о книге
]

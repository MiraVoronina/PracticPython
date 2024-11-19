from django.shortcuts import render
from django.http import Http404
from django.views import generic
from .models import Book, Author, BookInstance, Genre


# Главная страница
def index(request):
    """Главная страница сайта Local Library."""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context)


# Страница с перечнем всех книг
def book_list(request):
    """Страница с перечнем всех книг."""
    books = Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books})


# Страница с подробной информацией о книге
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['book_instances'] = BookInstance.objects.filter(book=book)
        return context

from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Genre(models.Model):
    """Model for book genres."""
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, Fantasy, etc.)")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)  # Using default=1 for existing author
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text="13-character ISBN number")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/catalog/book/{self.id}/"  # Example URL for the book detail page

class BookInstance(models.Model):
    """Model for book instances."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[('a', 'Available'), ('o', 'On loan')],
        default='a',
    )
    due_back = models.DateField(null=True, blank=True)
    imprint = models.CharField(max_length=200, help_text="Enter the imprint details (e.g. publisher)")
    id = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return f"{self.id} ({self.book.title})"

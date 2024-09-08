# Author model: Represents an author with a one-to-many relationship to books
# Fields: name (string), books (related books)

# Book model: Represents a book with a title, publication year, and a reference to an author
# Fields: title (string), publication_year (integer), author (foreign key to Author)

from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


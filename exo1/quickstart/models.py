from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    website = models.URLField()
    contact_email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.PositiveIntegerField()
    language = models.CharField(max_length=50)
    format = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='books')

    permissions = (
            ('view_book', 'Can view book'),
            ('change_book', 'Can change book'),
            ('delete_book', 'Can delete book'),
        )

    def __str__(self):
        return self.title

class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
    condition = models.CharField(max_length=50)
    acquisition_date = models.DateField()
    location = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book.title} - Copy {self.id}"

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE, related_name='loans')
    loan_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.book_copy.book.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    is_moderated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    rating_date = models.DateTimeField(auto_now_add=True)
    is_recommended = models.BooleanField(default=False)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} - {self.score}"
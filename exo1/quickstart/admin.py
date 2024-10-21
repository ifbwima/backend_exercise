from django.contrib import admin
from .models import Author, Publisher, Category, Book, BookCopy, Loan, Comment, Rating

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'date_of_birth')
    search_fields = ('name', 'nationality')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'contact_email')
    search_fields = ('name', 'contact_email')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'publication_date', 'language')
    list_filter = ('publication_date', 'language', 'category')
    search_fields = ('title', 'isbn', 'authors__name')

@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'condition', 'is_available')
    list_filter = ('condition', 'is_available')
    search_fields = ('book__title',)

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('user', 'book_copy', 'loan_date', 'due_date', 'status')
    list_filter = ('status', 'loan_date', 'due_date')
    search_fields = ('user__username', 'book_copy__book__title')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'publication_date', 'is_visible', 'is_moderated')
    list_filter = ('is_visible', 'is_moderated', 'publication_date')
    search_fields = ('user__username', 'book__title', 'content')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'score', 'rating_date')
    list_filter = ('score', 'rating_date')
    search_fields = ('user__username', 'book__title')
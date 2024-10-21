from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    min_publication_date = filters.DateFilter(field_name="publication_date", lookup_expr='gte')
    max_publication_date = filters.DateFilter(field_name="publication_date", lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'language', 'min_publication_date', 'max_publication_date']
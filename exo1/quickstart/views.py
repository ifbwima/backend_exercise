from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

from .models import Author, Publisher, Category, Book, BookCopy, Loan, Comment, Rating
from .serializers import AuthorSerializer, PublisherSerializer, CategorySerializer, BookSerializer, BookCopySerializer, LoanSerializer, CommentSerializer, RatingSerializer

from .serializers import BookSerializer, AuthorSerializer
from .filters import BookFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsAdminOrReadOnly, CanModifyBook
from rest_framework.permissions import IsAuthenticated

from guardian.shortcuts import get_objects_for_user
from rest_framework.permissions import IsAuthenticated
from guardian.core import ObjectPermissionChecker

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return get_objects_for_user(self.request.user, 'quickstart.view_book', Book)

    def check_object_permissions(self, request, obj):
        super().check_object_permissions(request, obj)
        checker = ObjectPermissionChecker(request.user)
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            if not checker.has_perm('change_book', obj):
                self.permission_denied(request)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'nationality']
    ordering_fields = ['name', 'date_of_birth']


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookCopyViewSet(viewsets.ModelViewSet):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
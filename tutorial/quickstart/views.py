from rest_framework import viewsets
from rest_framework import permissions

from quickstart.models import Author, Book
from quickstart.serializers import BookSerializer, AuthorSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LibraryView(BookViewSet):
    """
        API endpoint that allows books and their authors to be viewed or edited.
    """

    search_fields = ['writer_name', 'name']
    filter_backends = (filters.SearchFilter, )

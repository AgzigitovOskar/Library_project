import json

from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from core.models import Book, Reader, Author
from core.serializers import BookListRetrieveSerializer, ReaderListRetrieveSerializer, AuthorListRetrieveSerializer


def index(request):
    return HttpResponse("Библиотека")


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListRetrieveSerializer


class ReadersViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderListRetrieveSerializer


class AuthorsViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorListRetrieveSerializer

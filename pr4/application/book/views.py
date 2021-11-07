from rest_framework import generics

from application.book.models import Book

from application.book.serializer import BookSerializer


class  BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from django.urls import path

from application.book.views import BookListView

urlpatterns = [
    path('book-list/', BookListView.as_view()),
]
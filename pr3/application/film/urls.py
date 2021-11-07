from django.urls import path

from application.film.views import FilmListView

urlpatterns = [
    path('film-list/', FilmListView.as_view()),
]

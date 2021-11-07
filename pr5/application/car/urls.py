from django.urls import path

from application.car.views import CarListView

urlpatterns = [
    path('car-list/', CarListView.as_view()),
]

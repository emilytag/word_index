from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index/<str:word>", views.get_word, name="get_word"),
]
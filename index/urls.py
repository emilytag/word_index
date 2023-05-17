from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:word>/", views.get_word, name="get word"),
]
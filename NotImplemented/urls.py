# NotImplemented/urls.py

from django.urls import path
from NotImplemented import views

urlpatterns = [
    path("", views.NotImplemented, name='NotImplemented'),
]
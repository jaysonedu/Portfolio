from django.urls import path
from experience import views

urlpatterns = [
    path("", views.experience_page, name='experience'),
]
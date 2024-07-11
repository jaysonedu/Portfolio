from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# 7/8 first edit to views
def home(request):
    return render(request, "pages/home.html", {})


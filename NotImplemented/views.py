from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def NotImplemented(request):
    return render(request, 'NotImplemented/NotImplemented.html')



from django.urls import path
from .views import download_resume_page, download_resume

urlpatterns = [
    path('download-resume/', download_resume, name='download_resume'),
    path('', download_resume_page, name='resume_home'),
    path('download-resume/', download_resume, name='download_resume'),
]
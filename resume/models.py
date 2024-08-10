from django.db import models

# Create your models here.

class Resume(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.title


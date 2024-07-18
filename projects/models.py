from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technology = models.CharField(max_length=200)

    def __str__(self):
        return self.title

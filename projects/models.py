from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, blank=True)
    location = models.TextField(blank=True)
    timeframe = models.TextField(blank=True)
    overview = models.TextField(blank=True)
    description = models.TextField(blank=True)


    technology = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

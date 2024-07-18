from django.db import models

class HomePageContent(models.Model):
    heading = models.CharField(max_length=200, default="Hello, World!")
    about_me_title = models.CharField(max_length=100, default="About me")
    about_me_text = models.TextField(default="Hi! Welcome to my website! My name is Jason Qin, and I am currently studying Computer Science and Economics at Columbia University. Feel free to poke around and leave feedback!")
    headshot = models.ImageField(upload_to='headshots/', blank=True, null=True)

    def __str__(self):
        return "Home Page Content"

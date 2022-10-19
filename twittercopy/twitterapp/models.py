from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, default="", blank=True)

    def get_absolute_url(self):
        return "list"
    
    def __str__(self):
        return self.user.username

class Post(models.Model):
    content = models.CharField(max_length=200)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "list"
    
    def __str__(self):
        return self.author.user.username + " says " + self.content
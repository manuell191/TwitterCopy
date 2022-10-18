from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    bio = models.CharField(max_length=200, default="", blank=True)

    def get_absolute_url(self):
        return "list"

    def __str__(self):
        return self.username

class Post(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "list"

    def __str__(self):
        return self.user.username + " says " + self.content
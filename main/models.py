from django.db import models
import os

class users(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=105)

    def __str__(self):
        return [self.username,self.email ,self.password]

def filepath(request, filename):
    return os.path.join('uploads/', filename)

class photos(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=50, null=True)
    image = models.ImageField()

    def __str__(self):
        return [self.user_id, self.title,self.description, self.location, self.image]

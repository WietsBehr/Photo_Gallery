from django.db import models

class users(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=105)

    def __str__(self):
        return [self.username,self.email ,self.password]
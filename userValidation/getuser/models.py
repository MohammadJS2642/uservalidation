from django.db import models

# Create your models here.


class GettingUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
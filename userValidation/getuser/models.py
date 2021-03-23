from django.db import models

# Create your models here.

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ("MRS", 'Mrs.'),
    ('MS', 'Ms.'),
]


class GettingUserData(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=3, choices=TITLE_CHOICES)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

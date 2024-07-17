from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
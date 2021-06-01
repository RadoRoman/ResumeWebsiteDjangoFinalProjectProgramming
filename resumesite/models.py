from django.db import models


class Contact(models.Model):  # class for handling input from the website
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()

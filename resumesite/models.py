from django.db import models


class Contact(models.Model):  # class for handling user's input from the website's 'contact me' form
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()

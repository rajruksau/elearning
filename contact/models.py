from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField (max_length=254)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name
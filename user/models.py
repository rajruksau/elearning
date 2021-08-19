from django.db import models
from django.contrib.auth.models import User

class LoggedIn(models.Model):
    name = models.CharField('name', max_length=120)
    is_logged_in = models.BooleanField(blank= True, default=False)

    def __str__(self):
        return self.name
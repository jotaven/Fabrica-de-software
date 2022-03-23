from pickle import FALSE
from django.db import models

# Create your models here.
'''
Post:
    Titulo, Texto
'''

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)

    def __str__(self):
        return self.title
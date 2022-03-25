from django.db import models

# Create your models here.
'''
Post:
    Titulo, Texto
'''

class Post(models.Model):
    titulo = models.CharField(max_length=100, blank=False)
    texto = models.TextField(blank=False)

    def __str__(self):
        return self.titulo
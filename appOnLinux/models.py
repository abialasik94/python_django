from django.db import models

# Create your models here.
class Film(models.Model):
    tytul = models.CharField(max_length=32)

    def __str__(self):
        return self.tytul
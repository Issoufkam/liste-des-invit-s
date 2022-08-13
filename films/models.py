from django.db import models

# Create your models here.
class Invite(models.Model):
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    table = models.IntegerField()
    numero = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
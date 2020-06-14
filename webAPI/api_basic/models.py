from django.db import models

# Create your models here.

class wheatCanada(models.Model):
    year = models.IntegerField(primary_key=True)
    fdc = models.IntegerField()
    dc = models.IntegerField()
    fc = models.IntegerField()
    ah = models.IntegerField()

    def __str__(self):
        return self.year
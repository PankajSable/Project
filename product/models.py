from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=122)
    weight=models.CharField(max_length=122)
    price=models.CharField(max_length=122)
    createdat=models.DateField()
    updatedat=models.DateField()

    def __str__(self):
        return self.name
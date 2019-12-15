from django.conf import settings
from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=7)
    purchase = models.DecimalField(max_digits=2, decimal_places=2)
    selling = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return self.name


from django.db import models
from realtimequote.base_model import BaseModel



class Coin(BaseModel):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10 ,decimal_places=4, null=False, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(name="unique_name", fields=['name'])
        ]

from django.db import models
from realtimequote.base_model import BaseModel



class Coin(BaseModel):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=16 ,decimal_places=4, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(name="unique_name", fields=['name'])
        ]

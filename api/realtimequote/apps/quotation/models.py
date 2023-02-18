from django.db import models
from realtimequote.base_model import BaseModel
from apps.coin.models import Coin

class Quotation(BaseModel):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    min_price = models.DecimalField(max_digits=8, decimal_places=4, null=False, blank=False)
    max_price = models.DecimalField(max_digits=8, decimal_places=4, null=False, blank=False)
    variance = models.IntegerField(null=False, blank=False)
    create_date = models.DateField(null=False, blank=False)

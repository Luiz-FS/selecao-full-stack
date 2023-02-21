from apps.coin.models import Coin
from django.db import models

from realtimequote.base_model import BaseModel


class Quotation(BaseModel):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    min_price = models.DecimalField(max_digits=16, decimal_places=4, null=False, blank=False)
    max_price = models.DecimalField(max_digits=16, decimal_places=4, null=False, blank=False)
    variance = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    create_date = models.DateField(null=False, blank=False)

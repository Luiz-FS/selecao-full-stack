from django.contrib import admin
from apps.coin.models import Coin

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'created_at']
    list_filter = ['name', 'id']
    ordering = ['name', 'price', 'created_at']
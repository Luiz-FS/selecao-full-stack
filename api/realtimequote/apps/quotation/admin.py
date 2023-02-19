from django.contrib import admin
from apps.quotation.models import Quotation

@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ['id', 'coin', 'max_price', 'min_price', 'created_at']
    list_filter = ['coin', 'id']
    ordering = ['max_price', 'min_price', 'created_at']
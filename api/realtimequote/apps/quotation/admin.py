from apps.quotation.models import Quotation
from django.contrib import admin


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ["id", "coin", "max_price", "min_price", "created_at"]
    list_filter = ["coin", "id"]
    ordering = ["max_price", "min_price", "created_at"]

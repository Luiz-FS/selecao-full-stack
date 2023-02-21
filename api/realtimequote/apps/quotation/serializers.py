from apps.quotation.models import Quotation
from rest_framework import serializers


class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = "__all__"

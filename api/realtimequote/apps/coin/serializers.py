from rest_framework import serializers
from apps.coin.models import Coin


class CoinSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coin
        fields = '__all__'
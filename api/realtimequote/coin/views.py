from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from middlewares.authentication import JWTAuthentication
from coin.serializers import CoinSerializer
from coin.models import Coin
from coin.tasks import collect_coin_quotation


class CoinView(viewsets.ReadOnlyModelViewSet):
    queryset = Coin.objects.all().order_by("name")
    serializer_class = CoinSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_at']

    def get_paginated_response(self, data):
        result =  super().get_paginated_response(data)
        collect_coin_quotation.delay()
        return result




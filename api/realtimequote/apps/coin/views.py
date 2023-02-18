from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from middlewares.authentication import JWTAuthentication
from apps.coin.serializers import CoinSerializer
from apps.coin.models import Coin


class CoinView(viewsets.ReadOnlyModelViewSet):
    queryset = Coin.objects.all().order_by("name")
    serializer_class = CoinSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_at']


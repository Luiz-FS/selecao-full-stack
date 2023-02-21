from apps.coin.models import Coin
from apps.coin.serializers import CoinSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from middlewares.authentication import JWTAuthentication
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CoinView(viewsets.ReadOnlyModelViewSet):
    queryset = Coin.objects.all().order_by("name")
    serializer_class = CoinSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]

    @method_decorator(cache_page(30))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

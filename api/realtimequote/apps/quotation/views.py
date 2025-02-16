from apps.quotation.models import Quotation
from apps.quotation.serializers import QuotationSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from middlewares.authentication import JWTAuthentication
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class QuotationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quotation.objects.all().order_by("-create_date")
    serializer_class = QuotationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["coin__id", "create_date"]

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

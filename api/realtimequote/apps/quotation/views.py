from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from middlewares.authentication import JWTAuthentication
from apps.quotation.serializers import QuotationSerializer
from apps.quotation.models import Quotation


class QuotationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quotation.objects.all().order_by("create_date")
    serializer_class = QuotationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["coin", "create_date"]

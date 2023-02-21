import pytest
from datetime import datetime
from decimal import Decimal
from apps.coin.models import Coin
from apps.quotation.models import Quotation
from apps.quotation.repository import QuotationRepository
from apps.quotation.schemas import QuotationSchema


@pytest.mark.django_db
class TestQuotationRepository:
    def test_bulk_create_quotation(self):
        # arrange
        coin = Coin.objects.create(
            name="Coin", description="Coin description", price=Decimal("5.64")
        )
        quotations = [
            QuotationSchema(
                min_price=Decimal("5.00"),
                max_price=Decimal("5.64"),
                variance=Decimal("0.2"),
                create_date=datetime.now().date(),
            )
            for _ in range(10)
        ]

        # act
        QuotationRepository.bulk_create_quotation(quotations, coin)

        # assert
        assert len(Quotation.objects.all()) == len(quotations)

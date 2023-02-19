from apps.quotation.models import Quotation
from apps.quotation.schemas import QuotationSchema
from apps.coin.models import Coin


class QuotationRepository:
    @staticmethod
    def bulk_create_quotation(quotations: list[QuotationSchema], coin: Coin) -> None:
        quotations_entities = map(
            lambda quotation: Quotation(
                coin=coin,
                **quotation.dict()
            ),
            quotations
        )

        Quotation.objects.bulk_create(quotations_entities)

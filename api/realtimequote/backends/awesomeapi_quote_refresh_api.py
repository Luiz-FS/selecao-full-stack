import requests
from decimal import Decimal
from datetime import datetime

from backends.coin_quote_refresh_backend import CoinQuoteRefreshBackend
from apps.coin.schemas import CoinSchema
from apps.quotation.schemas import QuotationSchema
from simple_settings import settings


class AwesomeapiQuoteRefresh(CoinQuoteRefreshBackend):

    def get_current_quote(self) -> CoinSchema:
        url = f"{settings.AWESOMEAPI_URL}/json/last/{self.key}"

        response = requests.get(url)
        data = response.json()

        return CoinSchema(
            name=self.name,
            price=Decimal(data[self.data_key]["bid"]) 
        )

    
    def get_quote_history(self, days: int=1) -> list[QuotationSchema]:
        url = f"{settings.AWESOMEAPI_URL}/json/daily/{self.key}/{days}"

        response = requests.get(url)
        data = response.json()

        return list(
            map(
                lambda coin_quote: QuotationSchema(
                    min_price=Decimal(coin_quote["low"]),
                    max_price=Decimal(coin_quote["high"]),
                    variance=Decimal(coin_quote["pctChange"]),
                    create_date=datetime.fromtimestamp(int(coin_quote["timestamp"])).date()
                ),
                data
            )
        )

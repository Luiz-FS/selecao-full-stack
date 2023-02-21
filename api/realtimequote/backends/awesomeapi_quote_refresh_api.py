import logging
from decimal import Decimal
from datetime import datetime

from backends.coin_quote_refresh_backend import CoinQuoteRefreshBackend
from apps.coin.schemas import CoinSchema
from apps.quotation.schemas import QuotationSchema
from utils import requests
from simple_settings import settings


logger = logging.getLogger(__name__)


class AwesomeapiQuoteRefresh(CoinQuoteRefreshBackend):
    def get_current_quote(self) -> CoinSchema:
        logger.info(f"Fetching current quote of {self.name}")
        url = f"{settings.AWESOMEAPI_URL}/json/last/{self.key}"

        data = requests.get(url)

        return CoinSchema(name=self.name, price=Decimal(data[self.data_key]["bid"]))

    def get_quote_history(self, days: int = 1) -> list[QuotationSchema]:
        logger.info(f"Fetching the last {days} days of quote history of {self.name}")
        url = f"{settings.AWESOMEAPI_URL}/json/daily/{self.key}/{days}"

        data = requests.get(url)

        return list(
            map(
                lambda coin_quote: QuotationSchema(
                    min_price=Decimal(coin_quote["low"]),
                    max_price=Decimal(coin_quote["high"]),
                    variance=Decimal(coin_quote["pctChange"]),
                    create_date=datetime.fromtimestamp(int(coin_quote["timestamp"])).date(),
                ),
                data,
            )
        )

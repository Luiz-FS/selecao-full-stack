import logging
from decimal import Decimal
from simple_settings import settings

from backends.coin_quote_refresh_backend import CoinQuoteRefreshBackend
from backends.awesomeapi_quote_refresh_api import AwesomeapiQuoteRefresh
from apps.coin.schemas import CoinSchema
from apps.quotation.schemas import QuotationSchema
from utils import requests


logger = logging.getLogger(__name__)


class KrakenQuoteRefresh(CoinQuoteRefreshBackend):
    awesomeapi_coin_key: str

    def __init__(self, name, key, data_key, awesomeapi_coin_key):
        super().__init__(name, key, data_key)
        self.awesomeapi_coin_key = awesomeapi_coin_key

    def get_current_quote(self) -> CoinSchema:
        logger.info(f"Fetching current quote of {self.name}")
        url = f"{settings.KRAKEN_API_URL}/0/public/Ticker?pair={self.key}"

        data = requests.get(url)

        return CoinSchema(
            name=self.name,
            price=Decimal(data["result"][self.data_key]["a"][0]) 
        )

    
    def get_quote_history(self, days: int=1) -> list[QuotationSchema]:
        logger.info(f"Fetching the last {days} days of quote history of {self.name}")
        return AwesomeapiQuoteRefresh(
            name=self.name,
            key=self.awesomeapi_coin_key,
            data_key=""
        ).get_quote_history(days)
import requests
from decimal import Decimal

from backends.coin_quote_refresh_backend import CoinQuoteRefreshBackend
from apps.coin.schemas import CoinSchema
from realtimequote.settings import AWESOMEAPI_URL


class AwesomeapiQuoteRefresh(CoinQuoteRefreshBackend):
    data_key: str

    def __init__(self, name, key, data_key):
        super().__init__(name, key)
        self.data_key = data_key

    def get_current_quote(self) -> CoinSchema:
        url = f"{AWESOMEAPI_URL}/json/last/{self.key}"

        response = requests.get(url)
        data = response.json()

        return CoinSchema(
            name=self.name,
            price=Decimal(data[self.data_key]["bid"]) 
        )

    
    def get_quote_history(self):
        raise NotImplementedError()
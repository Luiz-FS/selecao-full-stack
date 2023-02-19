import requests
from decimal import Decimal

from realtimequote.settings import KRAKEN_API_URL
from backends.coin_quote_refresh_backend import CoinQuoteRefreshBackend
from apps.coin.schemas import CoinSchema

class KrakenQuoteRefresh(CoinQuoteRefreshBackend):
    data_key: str

    def __init__(self, name, key, data_key):
        super().__init__(name, key)
        self.data_key = data_key

    def get_current_quote(self) -> CoinSchema:
        url = f"{KRAKEN_API_URL}/0/public/Ticker?pair={self.key}"

        response = requests.get(url)
        data = response.json()

        return CoinSchema(
            name=self.name,
            price=Decimal(data["result"][self.data_key]["a"][0]) 
        )

    
    def get_quote_history(self):
        raise NotImplementedError()
from abc import ABC, abstractclassmethod
from apps.coin.schemas import CoinSchema
from apps.quotation.schemas import QuotationSchema


class CoinQuoteRefreshBackend(ABC):
    name: str
    key: str
    data_key: str

    def __init__(self, name, key, data_key):
        self.name = name
        self.key = key
        self.data_key = data_key

    @abstractclassmethod
    def get_current_quote(self) -> CoinSchema:  # pragma nocover
        raise NotImplementedError()
    
    def get_quote_history(self, days: int) -> list[QuotationSchema]:  # pragma nocover
        raise NotImplementedError()
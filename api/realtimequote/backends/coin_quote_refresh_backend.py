from abc import ABC, abstractclassmethod
from apps.coin.schemas import CoinSchema


class CoinQuoteRefreshBackend(ABC):
    name: str
    key: str

    def __init__(self, name, key):
        self.name = name
        self.key = key

    @abstractclassmethod
    def get_current_quote(self) -> CoinSchema:
        raise NotImplementedError()
    
    def get_quote_history(self):
        raise NotImplementedError()
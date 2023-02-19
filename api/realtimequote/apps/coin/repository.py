from apps.coin.models import Coin
from apps.coin.schemas import CoinSchema


class CoinRepository:
    @staticmethod
    def update_current_quote(current_quote: CoinSchema) -> None:
        Coin.objects.filter(name=current_quote.name).update(price=current_quote.price)

    @staticmethod
    def get_coin_by_name(name: str) -> Coin:
        return Coin.objects.filter(name=name).first()
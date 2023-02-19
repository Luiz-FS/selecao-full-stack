from apps.coin.models import Coin
from apps.coin.schemas import CoinSchema


class CoinRepository:
    def update_current_quote(current_quote: CoinSchema) -> None:
        Coin.objects.filter(name=current_quote.name).update(price=current_quote.price)
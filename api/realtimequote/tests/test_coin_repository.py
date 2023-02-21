from decimal import Decimal

import pytest
from apps.coin.models import Coin
from apps.coin.repository import CoinRepository
from apps.coin.schemas import CoinSchema


@pytest.mark.django_db
class TestCoinRepository:
    def test_update_current_quote(self):
        # arrange
        coin = Coin.objects.create(
            name="Coin", description="Coin description", price=Decimal("5.64")
        )

        coin_schema = CoinSchema(name=coin.name, price=Decimal("6.42"))

        # act
        CoinRepository.update_current_quote(coin_schema)

        # assert
        coin.refresh_from_db()
        assert coin.price == coin_schema.price

    def test_get_coin_by_name(self):
        # arrange
        coin = Coin.objects.create(
            name="Coin", description="Coin description", price=Decimal("5.64")
        )
        coin.refresh_from_db()

        # act
        result = CoinRepository.get_coin_by_name(coin.name)

        # assert
        assert result == coin

    def test_get_coin_by_name_not_found(self):
        # act
        result = CoinRepository.get_coin_by_name("Coin")

        # assert
        assert result is None

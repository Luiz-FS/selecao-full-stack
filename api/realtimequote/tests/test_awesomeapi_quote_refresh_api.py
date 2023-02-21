import pytest
from decimal import Decimal
from datetime import datetime
from apps.coin.schemas import CoinSchema
from apps.quotation.schemas import QuotationSchema
from backends.awesomeapi_quote_refresh_api import AwesomeapiQuoteRefresh
from simple_settings import settings


class TestAwesomeapiQuoteRefresh:
    def test_get_current_quote(self, mocker):
        # arrange
        coin = {"Coin": {"bid": "5.64"}}
        expected_result = CoinSchema(name="Coin", price=Decimal(coin["Coin"]["bid"]))

        mock_requests = mocker.patch("backends.awesomeapi_quote_refresh_api.requests")
        mock_requests.get.return_value = coin

        # act
        result = AwesomeapiQuoteRefresh(
            name="Coin", key="Coin", data_key="Coin"
        ).get_current_quote()

        # assert
        mock_requests.get.assert_called_with(f"{settings.AWESOMEAPI_URL}/json/last/Coin")

        assert result == expected_result

    def test_get_quote_history(self, mocker):
        # arrange
        quotations = [
            {
                "low": "5.00",
                "high": "5.64",
                "pctChange": "0.2",
                "timestamp": str(int(datetime.now().timestamp())),
            },
            {
                "low": "5.10",
                "high": "5.4",
                "pctChange": "0.2",
                "timestamp": str(int(datetime.now().timestamp())),
            },
        ]

        expected_result = list(
            map(
                lambda coin_quote: QuotationSchema(
                    min_price=Decimal(coin_quote["low"]),
                    max_price=Decimal(coin_quote["high"]),
                    variance=Decimal(coin_quote["pctChange"]),
                    create_date=datetime.fromtimestamp(int(coin_quote["timestamp"])).date(),
                ),
                quotations,
            )
        )

        mock_requests = mocker.patch("backends.awesomeapi_quote_refresh_api.requests")
        mock_requests.get.return_value = quotations

        # act
        result = AwesomeapiQuoteRefresh(name="Coin", key="Coin", data_key="Coin").get_quote_history(
            days=2
        )

        # assert
        mock_requests.get.assert_called_with(f"{settings.AWESOMEAPI_URL}/json/daily/Coin/2")

        assert result == expected_result

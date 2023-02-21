import pytest
from datetime import datetime
from celery.exceptions import MaxRetriesExceededError
from decimal import Decimal
from apps.quotation import tasks
from apps.quotation.tasks import collect_coin_quotation_history
from apps.quotation.schemas import QuotationSchema
from apps.coin.models import Coin
from utils.requests import RequestExeption


@pytest.fixture
def coin_to_backend_api_mock(backend_api_mock):
    tasks.COIN_TO_BACKEND_API = {"Coin": backend_api_mock(data_key="", name="", key="")}


class TestCollectCoinQuotationHistory:
    def test_when_expect_success(self, mocker, coin_to_backend_api_mock, backend_api_mock):
        # arrange
        coin = Coin()
        quotation = QuotationSchema(
            min_price=Decimal(5.00),
            max_price=Decimal(5.64),
            variance=Decimal(0.2),
            create_date=datetime.now().date(),
        )

        mock_get_quote_history = mocker.patch.object(
            backend_api_mock, "get_quote_history", return_value=[quotation]
        )
        mock_get_coin_by_name = mocker.patch(
            "apps.coin.tasks.CoinRepository.get_coin_by_name", return_value=coin
        )
        mock_bulk_create_quotation = mocker.patch(
            "apps.quotation.tasks.QuotationRepository.bulk_create_quotation"
        )

        # act
        task = collect_coin_quotation_history.delay(days=30)

        # assert
        mock_get_quote_history.assert_called_with(30)
        mock_get_coin_by_name.assert_called_with("Coin")
        mock_bulk_create_quotation.assert_called_with([quotation], coin)

        assert task.state == "SUCCESS"

    def test_when_occours_request_exception(
        self, mocker, coin_to_backend_api_mock, backend_api_mock
    ):
        # arrange
        mock_get_quote_history = mocker.patch.object(
            backend_api_mock, "get_quote_history", side_effect=RequestExeption()
        )
        mock_get_coin_by_name = mocker.patch("apps.coin.tasks.CoinRepository.get_coin_by_name")

        # act
        task = collect_coin_quotation_history.delay(30)

        # assert
        mock_get_quote_history.assert_called_with(30)
        mock_get_coin_by_name.assert_called_with("Coin")
        assert mock_get_quote_history.call_count == collect_coin_quotation_history.max_retries + 1

        assert task.state == "FAILURE"
        assert isinstance(task.result, MaxRetriesExceededError)

    def test_when_occours_unexpected_exception(
        self, mocker, coin_to_backend_api_mock, backend_api_mock
    ):
        # arrange
        mock_get_quote_history = mocker.patch.object(
            backend_api_mock, "get_quote_history", side_effect=Exception()
        )
        mock_get_coin_by_name = mocker.patch("apps.coin.tasks.CoinRepository.get_coin_by_name")

        # act
        task = collect_coin_quotation_history.delay(30)

        # assert
        mock_get_quote_history.assert_called_with(30)
        mock_get_coin_by_name.assert_called_with("Coin")

        assert task.state == "FAILURE"
        assert isinstance(task.result, Exception)

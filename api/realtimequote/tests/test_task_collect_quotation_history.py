import pytest
from celery.exceptions import MaxRetriesExceededError
from decimal import Decimal
from apps.coin import tasks
from apps.coin.tasks import collect_coin_quotation
from apps.coin.schemas import CoinSchema
from utils.requests import RequestExeption


@pytest.fixture
def coin_to_backend_api_mock(backend_api_mock):
    tasks.COIN_TO_BACKEND_API = {
        "Coin": backend_api_mock(data_key="", name="", key="")
    }


class TestCollectCoinQuotation:

    def test_when_expect_success(self, mocker, coin_to_backend_api_mock, backend_api_mock):
        # arrange
        coin = CoinSchema(name="Coin", price=Decimal(5.64))

        mock_get_current_quote = mocker.patch.object(backend_api_mock, "get_current_quote", return_value=coin)
        mock_update_current_quote = mocker.patch("apps.coin.tasks.CoinRepository.update_current_quote")

        # act
        task = collect_coin_quotation.delay()

        # assert
        mock_get_current_quote.asset_called()
        mock_update_current_quote.assert_called_with(coin)

        assert task.state == 'SUCCESS'
    
    def test_when_occours_request_exception(self, mocker, coin_to_backend_api_mock, backend_api_mock):
        # arrange
        mock_get_current_quote = mocker.patch.object(backend_api_mock, "get_current_quote", side_effect=RequestExeption())

        # act
        task = collect_coin_quotation.delay()

        # assert
        assert task.state == 'FAILURE'
        assert isinstance(task.result, MaxRetriesExceededError)
        assert mock_get_current_quote.call_count == collect_coin_quotation.max_retries + 1
    
    def test_when_occours_unexpected_exception(self, mocker, coin_to_backend_api_mock, backend_api_mock):
        # arrange
        mocker.patch.object(backend_api_mock, "get_current_quote", side_effect=Exception())

        # act
        task = collect_coin_quotation.delay()

        # assert
        assert task.state == 'FAILURE'
        assert isinstance(task.result, Exception)



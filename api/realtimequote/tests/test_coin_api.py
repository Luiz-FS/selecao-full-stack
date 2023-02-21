import pytest
from http import HTTPStatus
from apps.coin.serializers import CoinSerializer


@pytest.mark.django_db
class TestList:
    def test_list_coins(self, client, make_coins, authenticator_mock):
        # arrange
        authenticator_mock(success=True)
        expected_coins = CoinSerializer(make_coins, many=True).data
        expected_coins = sorted(expected_coins, key=lambda coin: coin["name"])

        # act
        response = client.get("/api/coin/")
        data = response.json()

        #assert
        assert expected_coins == data["results"]
    
    def test_list_coins_empty(self, client, authenticator_mock):
        # arrange
        authenticator_mock(success=True)
        expected_coins = []

        # act
        response = client.get("/api/coin/")
        data = response.json()

        #assert
        assert expected_coins == data["results"]

    def test_list_coins_unauthorized(self, client, authenticator_mock):
        # arrange
        authenticator_mock(success=False)

        # act
        response = client.get("/api/coin/")

        # assert
        assert response.status_code == HTTPStatus.UNAUTHORIZED
import pytest
from decimal import Decimal
from datetime import datetime
from django.contrib.auth.models import User
from apps.coin.models import Coin
from apps.quotation.models import Quotation
from backends.coin_quote_refresh_backend import CoinQuoteRefreshBackend


class ResponseMock:
    status_code = 200

    def __init__(self, status_code):
        self.status_code = status_code

    def json(self):  # pragma nocover
        return {}


class RequestMock:
    headers = {}
    session = {}

    def __init__(self, headers, session):
        self.headers = headers
        self.session = session


class BackendApiMock(CoinQuoteRefreshBackend):
    def get_current_quote(self):  # pragma nocover
        ...

    def get_quote_history(self, days: int):  # pragma nocover
        ...


@pytest.fixture
def make_coins():
    return [
        Coin.objects.create(name=f"coin{i}", description="Coin description", price=Decimal(5.64))
        for i in range(10)
    ]


@pytest.fixture
def make_quotations(make_coins):
    return [
        Quotation.objects.create(
            coin=make_coins[i],
            min_price=Decimal(5.00),
            max_price=Decimal(5.64),
            variance=Decimal(0.2),
            create_date=datetime.now().date(),
        )
        for i in range(10)
    ]


@pytest.fixture
def authenticator_mock(mocker):
    def mock_value(success=True):
        user = User(id=1, email="test@test.com")

        if success:
            return_value = (user, None)
        else:
            return_value = None

        mocker.patch(
            "middlewares.authentication.JWTAuthentication.authenticate", return_value=return_value
        )
        return user

    return mock_value


@pytest.fixture
def request_mock():
    return RequestMock


@pytest.fixture
def response_mock():
    return ResponseMock


@pytest.fixture
def backend_api_mock():
    return BackendApiMock

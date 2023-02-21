import pytest
from requests import ConnectionError, Timeout
from utils import requests


class TestRequestsGet:
    def test_when_expect_success(self, mocker, response_mock):
        # arrange
        request_mock = mocker.patch("utils.requests.requests")
        request_mock.get.return_value = response_mock(status_code=200)

        # act
        result = requests.get("url")

        # assert
        request_mock.get.assert_called_with("url")
        assert result == {}

    def test_when_expect_fail_by_status(self, mocker, response_mock):
        # arrange
        request_mock = mocker.patch("utils.requests.requests")
        request_mock.get.return_value = response_mock(status_code=400)

        # act / assert
        with pytest.raises(requests.RequestExeption):
            requests.get("url")

    @pytest.mark.parametrize(
        "error",
        [
            ConnectionError(),
            Timeout()
        ]
    )
    def test_when_expect_raise_request_exception(self, mocker, error):
        # arrange
        request_mock = mocker.patch("utils.requests.requests")
        request_mock.get.side_effect = error

        # act / assert
        with pytest.raises(requests.RequestExeption):
            requests.get("url")
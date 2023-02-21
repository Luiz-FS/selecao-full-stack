import pytest
from http import HTTPStatus
from apps.quotation.serializers import QuotationSerializer


@pytest.mark.django_db
class TestList:
    def test_list_quotations(self, client, make_quotations, authenticator_mock):
        # arrange
        authenticator_mock(success=True)
        expected_quotations = QuotationSerializer(make_quotations, many=True).data
        expected_quotations = sorted(
            expected_quotations, key=lambda quotation: quotation["create_date"], reverse=True
        )

        for quotation in expected_quotations:
            quotation["coin"] = str(quotation["coin"])

        # act
        response = client.get("/api/quotation/")
        data = response.json()

        # assert
        assert expected_quotations == data["results"]

    def test_list_quotations_empty(self, client, authenticator_mock):
        # arrange
        authenticator_mock(success=True)
        expected_quotations = []

        # act
        response = client.get("/api/quotation/")
        data = response.json()

        # assert
        assert expected_quotations == data["results"]

    def test_list_quotations_unauthorized(self, client, authenticator_mock):
        # arrange
        authenticator_mock(success=False)

        # act
        response = client.get("/api/quotation/")

        # assert
        assert response.status_code == HTTPStatus.UNAUTHORIZED

import os
import unittest
from copy import deepcopy

import pytest
from dotenv import load_dotenv

from culqi import __version__
from culqi.client import Culqi
from culqi.resources import Token
from culqi.utils.errors import ErrorMessage, NotAllowedError

from .data import Data


class TokenTest(unittest.TestCase):
    # pylint: disable = too-many-public-methods
    def __init__(self, *args, **kwargs):
        super(TokenTest, self).__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__
        self.public_key = os.environ.get("API_PUBLIC_KEY")
        self.private_key = os.environ.get("API_PRIVATE_KEY")
        self.culqi = Culqi(self.public_key, self.private_key)
        self.token = Token(client=self.culqi)

        self.metadata = {"order_id": "0001"}

    @staticmethod
    def get_token_data(code, provider):
        return deepcopy(Data.CARD[code][provider])

    def test_url(self):
        # pylint: disable = protected-access
        id_ = "sample_id"

        assert self.token._get_url() == "https://api.culqi.com/v2/tokens"
        assert self.token._get_url(id_) == "https://api.culqi.com/v2/tokens/{0}".format(
            id_
        )

    @pytest.mark.vcr()
    def test_token_create(self):
        token_data = self.get_token_data("successful", "visa")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create_with_custom_headers(self):
        token_data = self.get_token_data("successful", "visa")
        token = self.token.create(
            data=token_data,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/80.0.3987.122 Safari/537.36"
                )
            },
        )
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_retrieve(self):
        token_data = self.get_token_data("successful", "visa")
        created_token = self.token.create(data=token_data)
        retrieved_token = self.token.read(created_token["data"]["id"])
        assert created_token["data"]["id"] == retrieved_token["data"]["id"]

    @pytest.mark.vcr()
    def test_token_list(self):
        retrieved_token_list = self.token.list()
        assert "items" in retrieved_token_list["data"]

    @pytest.mark.vcr()
    def test_token_update(self):
        token_data = self.get_token_data("successful", "visa")
        created_token = self.token.create(data=token_data)

        metadatada = {"metadata": self.metadata}
        updated_token = self.token.update(
            id_=created_token["data"]["id"], data=metadatada
        )

        assert created_token["data"]["id"] == created_token["data"]["id"]
        assert updated_token["data"]["metadata"] == self.metadata

    @pytest.mark.vcr()
    def test_token_delete(self):
        with pytest.raises(NotAllowedError) as excinfo:
            token_data = self.get_token_data("successful", "visa")
            token = self.token.create(data=token_data)
            self.token.delete(token["data"]["id"])

        assert ErrorMessage.NOT_ALLOWED in str(excinfo.value)

    @pytest.mark.vcr()
    def test_token_create__successful__visa(self):
        token_data = self.get_token_data("successful", "visa")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create__successful__master_card(self):
        token_data = self.get_token_data("successful", "master_card")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create__successful__american_express(self):
        token_data = self.get_token_data("successful", "american_express")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create__successful__diners_club(self):
        token_data = self.get_token_data("successful", "diners_club")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create__stolen_card__visa(self):
        token_data = self.get_token_data("stolen_card", "visa")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create__lost_card__visa(self):
        token_data = self.get_token_data("lost_card", "visa")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create__insufficient_funds__visa(self):
        token_data = self.get_token_data("insufficient_funds", "visa")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create__contact_issuer__master_card(self):
        token_data = self.get_token_data("contact_issuer", "master_card")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create__incorrect_cvv__master_card(self):
        token_data = self.get_token_data("incorrect_cvv", "master_card")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create__issuer_not_available__american_express(self):
        token_data = self.get_token_data("issuer_not_available", "american_express")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create__issuer_decline_operation__american_express(self):
        token_data = self.get_token_data("issuer_decline_operation", "american_express")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create__invalid_card__diners_club(self):
        token_data = self.get_token_data("invalid_card", "diners_club")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    @pytest.mark.vcr()
    def test_token_create__processing_error__diners_club(self):
        token_data = self.get_token_data("processing_error", "diners_club")
        token = self.token.create(data=token_data)
        assert token["data"]["object"] == "token"

    # This fail due to Internal server error in Culqi
    # @pytest.mark.vcr()
    # def test_token_create__fraudulent__diners_club(self):
    #     token_data = self.get_token_data(
    #         "fraudulent", "diners_club")
    #     token = self.token.create(data=token_data)
    #     assert token["data"]["object"] == "token"


if __name__ == "__main__":
    unittest.main()

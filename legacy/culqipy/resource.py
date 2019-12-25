# pylint: disable=import-outside-toplevel
from .utils import RequestMethodError, Util

class Operation():

    @staticmethod
    def list(url, params=None, key=None):
        return Util(
            url=url,
            data=params,
            method="GET",
            key=key,
        ).json_result()

    @staticmethod
    def create(url, body, key=None):
        return Util(
            url=url,
            data=body,
            method="POST",
            key=key,
        ).json_result()

    @staticmethod
    def get_delete(url, id_, method, key=None):
        """
        Get or delete, just change the method: "GET" or "DELETE".
        """
        return Util(
            url=url + id_ + "/",
            method=method,
            key=key,
        ).json_result()

    @staticmethod
    def update(url, id_, body=None, key=None):
        return Util(
            url=url + id_ + "/",
            method="PATCH",
            data=body,
            key=key,
        ).json_result()


class BaseResource:
    """Parent class for all the resources."""

    URL = None

    @classmethod
    def list(cls, params=None):
        return Operation.list(cls.URL, params)

    @classmethod
    def create(cls, body):
        return Operation.create(cls.URL, body)

    @classmethod
    def get(cls, id_):
        return Operation.get_delete(cls.URL, id_, "GET")

    @classmethod
    def delete(cls, id_):
        return Operation.get_delete(cls.URL, id_, "DELETE")

    @classmethod
    def update(cls, id_, body):
        return Operation.update(cls.URL, id_, body)


class Card(BaseResource):

    URL = "/cards/"


class Event(BaseResource):

    URL = "/events/"

    @classmethod
    def create(cls, body):
        raise RequestMethodError()

    @classmethod
    def delete(cls, id_):
        raise RequestMethodError()

    @classmethod
    def update(cls, id_, body):
        raise RequestMethodError()


class Customer(BaseResource):

    URL = "/customers/"


class Transfer(Event):

    URL = "/transfers/"


class Iins(Event):

    URL = "/iins/"


class Token(BaseResource):

    URL = "/tokens/"

    @staticmethod
    def create(body):
        from . import public_key

        # A tokens need the public_key to be created.
        return Operation.create(Token.URL, body, public_key)

    @classmethod
    def delete(cls, id_):
        raise RequestMethodError()


class Charge(BaseResource):

    URL = "/charges/"

    @classmethod
    def delete(cls, id_):
        raise RequestMethodError()

    @staticmethod
    def capture(id_):
        return Util(
            url=Charge.URL + id_ + "/capture/",
            data="",
            method="POST",
        ).json_result()


class Plan(BaseResource):

    URL = "/plans/"


class Subscription(BaseResource):

    URL = "/subscriptions/"


class Refund(BaseResource):

    URL = "/refunds/"

    @classmethod
    def delete(cls, id_):
        raise RequestMethodError()

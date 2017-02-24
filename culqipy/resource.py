import culqipy

from culqipy.utils import RequestMethodError, Util


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
    def get_delete(url, id, method, key=None):
        """
        Get or delete, just change the method: "GET" or "DELETE".
        """
        return Util(
            url=url + id + "/",
            method=method,
            key=key,
        ).json_result()

    @staticmethod
    def update(url, id, body=None, key=None):
        return Util(
            url=url + id + "/",
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
    def get(cls, id):
        return Operation.get_delete(cls.URL, id, "GET")

    @classmethod
    def delete(cls, id):
        return Operation.get_delete(cls.URL, id, "DELETE")

    @classmethod
    def update(cls, id, body):
        return Operation.update(cls.URL, id, body)


class Card(BaseResource):

    URL = "/cards/"


class Event(BaseResource):

    URL = "/events/"

    @classmethod
    def create(cls, body):
        raise RequestMethodError()

    @classmethod
    def delete(cls, id):
        raise RequestMethodError()

    @classmethod
    def update(cls, id, body):
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
        # A tokens need the public_key to be created.
        return Operation.create(Token.URL, body, culqipy.public_key)

    @classmethod
    def delete(cls, id):
        raise RequestMethodError()


class Charge(BaseResource):

    URL = "/charges/"

    @classmethod
    def delete(cls, id):
        raise RequestMethodError()

    @staticmethod
    def capture(id):
        return Util(
            url=Charge.URL + id + "/capture/",
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
    def delete(cls, id):
        raise RequestMethodError()

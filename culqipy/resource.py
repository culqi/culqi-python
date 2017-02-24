import culqipy

from culqipy.utils import Util


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


class Card:
    URL = "/cards/"

    @staticmethod
    def create(body):
        return Operation.create(Card.URL, body)

    @staticmethod
    def delete(id):
        return Operation.get_delete(Card.URL, id, "DELETE")

    @staticmethod
    def get(id):
        return Operation.get_delete(Card.URL, id, "GET")

    @staticmethod
    def update(id, body):
        return Operation.update(Card.URL, id, body)


class Event:
    URL = "/events/"

    @staticmethod
    def list(params=None):
        return Operation.list(Event.URL, params)

    @staticmethod
    def get(id):
        return Operation.get_delete(Event.URL, id, "GET")


class Customer:
    URL = "/customers/"

    @staticmethod
    def list(params=None):
        return Operation.list(Customer.URL, params)

    @staticmethod
    def create(body):
        return Operation.create(Customer.URL, body)

    @staticmethod
    def delete(id):
        return Operation.get_delete(Customer.URL, id, "DELETE")

    @staticmethod
    def get(id):
        return Operation.get_delete(Customer.URL, id, "GET")

    @staticmethod
    def update(id, body):
        return Operation.update(Customer.URL, id, body)


class Transfer:
    URL = "/transfers/"

    @staticmethod
    def list(params=None):
        return Operation.list(Transfer.URL, params)

    @staticmethod
    def get(id):
        return Operation.get_delete(Transfer.URL, id, "GET")


class Iins:
    URL = "/iins/"

    @staticmethod
    def list(params):
        return Operation.list(Iins.URL, params)

    @staticmethod
    def get(id):
        return Operation.get_delete(Iins.URL, id, "GET")


class Token:
    URL = "/tokens/"

    @staticmethod
    def list(params=None):
        return Operation.list(Token.URL, params)

    @staticmethod
    def create(body):
        # A tokens need the public_key to be created.
        return Operation.create(Token.URL, body, culqipy.public_key)

    @staticmethod
    def get(id):
        return Operation.get_delete(Token.URL, id, "GET")


class Charge:
    URL = "/charges/"

    @staticmethod
    def list(params=None):
        return Operation.list(Charge.URL, params)

    @staticmethod
    def create(body):
        return Operation.create(Charge.URL, body)

    @staticmethod
    def get(id):
        return Operation.get_delete(Charge.URL, id, "GET")

    @staticmethod
    def capture(id):
        return Util(
            url=Charge.URL + id + "/capture/",
            data="",
            method="POST",
        ).json_result()

    @staticmethod
    def update(id, body):
        return Operation.update(Charge.URL, id, body)


class Plan:
    URL = "/plans/"

    @staticmethod
    def list(params=None):
        return Operation.list(Plan.URL, params)

    @staticmethod
    def create(body):
        return Operation.create(Plan.URL, body)

    @staticmethod
    def delete(id):
        return Operation.get_delete(Plan.URL, id, "DELETE")

    @staticmethod
    def get(id):
        return Operation.get_delete(Plan.URL, id, "GET")

    @staticmethod
    def update(id, body):
        return Operation.update(Plan.URL, id, body)


class Subscription:
    URL = "/subscriptions/"

    @staticmethod
    def list(params=None):
        return Operation.list(Subscription.URL, params)

    @staticmethod
    def create(body):
        return Operation.create(Subscription.URL, body)

    @staticmethod
    def delete(id):
        return Operation.get_delete(Subscription.URL, id, "DELETE")

    @staticmethod
    def get(id):
        return Operation.get_delete(Subscription.URL, id, "GET")

    @staticmethod
    def update(id, body):
        return Operation.update(Subscription.URL, id, body)


class Refund:
    URL = "/refunds/"

    @staticmethod
    def list(params=None):
        return Operation.list(Refund.URL, params)

    @staticmethod
    def create(body):
        return Operation.create(Refund.URL, body)

    @staticmethod
    def get(id):
        return Operation.get_delete(Refund.URL, id, "GET")

    @staticmethod
    def update(id, body):
        return Operation.update(Refund.URL, id, body)

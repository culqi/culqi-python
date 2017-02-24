import culqipy
import json
import requests


class Util:

    def __init__(self, url, method, data=None, key=None):
        """
        Init the arguments for a request.

        The key by default is the secret key. It can also be the
        public key in case we want to create a token.
        """

        self.url = culqipy.API_URL + url
        # Validating the method.
        self.method = method.upper()
        if self.method not in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            raise ValueError('Method not allowed.')
        # Setting the payload.
        self.data = None
        if data:
            self.data = json.dumps(data)
        # Setting the secret_key by default.
        self.key = key
        if not key:
            self.key = culqipy.secret_key

    def json_result(self):
        """
        Returns the response as a dict if the response has content. Otherwise,
        returns the http response object.
        """

        response = self.get_result()
        # Returns a json dict or and object if the response does not have
        # content.
        return self.json_or_object(response)

    def get_result(self):
        """
        Returns an http response object.
        """

        timeout = 60
        if self.method == "GET":
            timeout = 360

        headers = {
            "Authorization": "Bearer " + self.key,
            "content-type": "application/json"
        }
        response = None
        try:
            response = getattr(requests, self.method.lower())(
                self.url,
                headers=headers,
                params=self.data,
                data=self.data,
                timeout=timeout,
            )
            # Return the response.
            return response
        except requests.exceptions.RequestException:
            error = {
                "object": "error",
                "type": "server",
                "code": "404",
                "message": "connection...",
                "user_message": "Connection Error!",
            }
            return error

    @classmethod
    def json_or_object(cls, response):
        """
        Returns the content of the response as a dict. If the object
        does not have content, then returns the response itself.
        """
        try:
            return response.json()  # Returns a dict.
        except:
            # If response does not have content.
            return response


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


Card = Card()


class Event:
    URL = "/events/"

    @staticmethod
    def list(params=None):
        return Operation.list(Event.URL, params)

    @staticmethod
    def get(id):
        return Operation.get_delete(Event.URL, id, "GET")


Event = Event()


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


Customer = Customer()


class Transfer:
    URL = "/transfers/"

    @staticmethod
    def list(params=None):
        return Operation.list(Transfer.URL, params)

    @staticmethod
    def get(id):
        return Operation.get_delete(Transfer.URL, id, "GET")


Transfer = Transfer()


class Iins:
    URL = "/iins/"

    @staticmethod
    def list(params):
        return Operation.list(Iins.URL, params)

    @staticmethod
    def get(id):
        return Operation.get_delete(Iins.URL, id, "GET")


Iins = Iins()


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


Token = Token()


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


Charge = Charge()


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


Plan = Plan()


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


Subscription = Subscription()


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


Refund = Refund()

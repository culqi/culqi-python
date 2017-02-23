import culqipy
import json
import requests


class Util:

    @staticmethod
    def json_result(url, data, method, key=None):
        """
        Returns an http response object.

        The key by default is the secret key. It can also be the
        public key in case we want to create a token.
        """

        timeout = 60
        if method.upper() == "GET":
            timeout = 360

        # Setting the secret_key by default.
        if not key:
            key = culqipy.secret_key

        headers = {
            "Authorization": "Bearer " + key,
            "content-type": "application/json"
        }
        r = ""
        try:
            if method.upper() == "GET":
                if not data:
                    r = requests.get(
                        culqipy.API_URL + url,
                        headers=headers,
                        timeout=timeout,
                    )
                else:
                    r = requests.get(
                        culqipy.API_URL + url,
                        headers=headers,
                        params=json.dumps(data),
                        timeout=timeout,
                    )
            if method.upper() == "POST":
                r = requests.post(
                    culqipy.API_URL + url,
                    headers=headers,
                    data=json.dumps(data),
                    timeout=timeout,
                )
            if method.upper() == "DELETE":
                r = requests.delete(
                    culqipy.API_URL + url,
                    headers=headers,
                    timeout=timeout,
                )
            if method.upper() == "PATCH":
                r = requests.patch(
                    culqipy.API_URL + url,
                    headers=headers,
                    data=json.dumps(data),
                    timeout=timeout,
                )
            r.raise_for_status()
            return r
        except (requests.exceptions.RequestException,
                requests.exceptions.HTTPError):
            error = {
                "object": "error",
                "type": "server",
                "code": "404",
                "message": "connection...",
                "user_message": "Connection Error!",
            }
            return json.dumps(error)


class CulqiError(Exception):
    def __init__(self, response_error):
        self.response_error = response_error


class Operation():
    @staticmethod
    def list(url, params, key=None):
        try:
            response = Util().json_result(
                url, params, "GET", key,
            )
            return response.json()
        except CulqiError as ce:
            return ce.response_error

    @staticmethod
    def create(url, body, key=None):
        try:
            response = Util().json_result(
                url, body, "POST", key,
            )
            if response.json().get("object") == "error":
                raise CulqiError(response.json())
            return response.json()
        except CulqiError as ce:
            return ce.response_error

    @staticmethod
    def get_delete(url, id, method, key=None):
        try:
            response = Util().json_result(
                url + id + "/", "", method, key,
            )
            if response.json().get("object") == "error":
                raise CulqiError(response.json())
            return response.json()
        except CulqiError as ce:
            return ce.response_error

    @staticmethod
    def update(url, id, body, key=None):
        try:
            response = Util().json_result(
                url + id + "/", body, "PATCH", key,
            )
            if response.json().get("object") == "error":
                raise CulqiError(response.json())
            return response.json()
        except CulqiError as ce:
            return ce.response_error


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
    def list(params):
        return Operation.list(Event.URL, params)

    @staticmethod
    def get(id):
        return Operation.get_delete(Event.URL, id, "GET")


Event = Event()


class Customer:
    URL = "/customers/"

    @staticmethod
    def list(params):
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
    def list(params):
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
    def list(params):
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
    def list(params):
        return Operation.list(Charge.URL, params)

    @staticmethod
    def create(body):
        return Operation.create(Charge.URL, body)

    @staticmethod
    def get(id):
        return Operation.get_delete(Charge.URL, id, "GET")

    @staticmethod
    def capture(id):
        try:
            response = Util().json_result(
                Charge.URL + id + "/capture/", "", "POST")
            if response.json().get("object") == "error":
                raise CulqiError(response.json())
            return response.json()
        except CulqiError as ce:
            return ce.response_error

    @staticmethod
    def update(id, body):
        return Operation.update(Charge.URL, id, body)


Charge = Charge()


class Plan:
    URL = "/plans/"

    @staticmethod
    def list(params):
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
    def list(params):
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
    def list(params):
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

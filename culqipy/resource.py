import culqipy
import requests
import json


class Util:
    @staticmethod
    def json_result(self, key, url, data, method):
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
                        timeout=60
                    )
                else:
                    r = requests.get(
                        culqipy.API_URL + url,
                        headers=headers,
                        params=json.dumps(data),
                        timeout=60
                    )
            if method.upper() == "POST":
                r = requests.post(
                        culqipy.API_URL + url,
                        headers=headers,
                        data=json.dumps(data),
                        timeout=60
                    )
            if method.upper() == "DELETE":
                r = requests.delete(
                        culqipy.API_URL + url,
                        headers=headers,
                        timeout=60
                    )
            return r.json()
        except requests.exceptions.RequestException:
            error = {"object": "error", "type": "server", "code": "404",
                      "message": "connection...",
                     "user_message": "No encuentra el servidor"}
            return json.dumps(error)


class ObjectHelper:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Transfer:
    URL = "/transfers/"

    @staticmethod
    def list(params):
        return Util().json_result(
                culqipy.API_KEY,
                Transfer.URL,
                params, "GET")

    @staticmethod
    def get(id):
        return Util().json_result(
                culqipy.API_KEY,
                Transfer.URL + id + "/",
                "", "GET")

Transfer = Transfer()


class Iins:
    URL = "/iins/"

    @staticmethod
    def get(id):
        return Util().json_result(
                culqipy.API_KEY,
                Iins.URL + id + "/",
                "", "GET")

Iins = Iins()


class Token:
    URL = "/tokens/"

    @staticmethod
    def create(body):
        return Util().json_result(
            culqipy.COD_COMMERCE,
            Token.URL,
            body, "POST")

    @staticmethod
    def get(id):
        return Util().json_result(
                culqipy.API_KEY,
                Token.URL + id + "/",
                "", "GET")


Token = Token()


class Charge:
    URL = "/charges/"

    @staticmethod
    def list(params):
        return Util().json_result(
                culqipy.API_KEY,
                Charge.URL,
                params, "GET")

    @staticmethod
    def create(body):
        return Util().json_result(
                culqipy.API_KEY,
                Charge.URL,
                body, "POST")

    @staticmethod
    def get(id):
        return Util().json_result(
                culqipy.API_KEY,
                Charge.URL + id + "/",
                "", "GET")

Charge = Charge()


class Plan:
    URL = "/plans/"

    @staticmethod
    def list(params):
        return Util().json_result(
                culqipy.API_KEY,
                Plan.URL,
                params, "GET")

    @staticmethod
    def create(body):
        return Util().json_result(
                culqipy.API_KEY,
                Plan.URL,
                body, "POST")

    @staticmethod
    def get(id):
        return Util().json_result(
                culqipy.API_KEY,
                Plan.URL + id + "/",
                "", "GET")

Plan = Plan()


class Subscription:
    URL = "/subscriptions/"

    @staticmethod
    def list( params):
        return Util().json_result(
                culqipy.API_KEY,
                Subscription.URL,
                params, "GET")

    @staticmethod
    def create(body):
        return Util().json_result(
                culqipy.API_KEY,
                Subscription.URL,
                body, "POST")

    @staticmethod
    def delete(id):
        return Util().json_result(
                culqipy.API_KEY,
                Subscription.URL + id + "/",
                "", "DELETE")

    @staticmethod
    def get(id):
        return Util().json_result(
                culqipy.API_KEY,
                Subscription.URL + id + "/",
                "", "GET")

Subscription = Subscription()


class Refund:
    URL = "/refunds/"

    @staticmethod
    def list(params):
        return Util().json_result(
                culqipy.API_KEY,
                Refund.URL,
                params, "GET")

    @staticmethod
    def create(body):
        return Util().json_result(
                culqipy.API_KEY,
                Refund.URL,
                body, "POST")

    @staticmethod
    def get(id):
        return Util().json_result(
                culqipy.API_KEY,
                Refund.URL + id + "/",
                "", "GET")

Refund = Refund()

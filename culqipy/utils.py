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
            raise RequestMethodError()
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

    @staticmethod
    def json_or_object(response):
        """
        Returns the content of the response as a dict. If the object
        does not have content, then returns the response itself.
        """
        try:
            return response.json()  # Returns a dict.
        except:
            # If response does not have content.
            return response


class RequestMethodError(Exception):
    """Raised when a invalid method is executed."""

    error_message = 'Method not allowed.'

    def __init__(self):
        super(RequestMethodError, self).__init__(self.error_message)

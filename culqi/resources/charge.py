from culqi.utils.errors import ErrorMessage, NotAllowedError
from culqi.utils.urls import URL
from culqi.resources.base import Resource

__all__ = ["Charge"]


class Charge(Resource):
    endpoint = URL.CHARGE

    def delete(self, id_, data=None, **options):
        raise NotAllowedError(ErrorMessage.NOT_ALLOWED)

    def capture(self, id_, data=None, **options):
        headers = {}
        if("rsa_public_key" in options and "rsa_id" in options):
            data = self._encrypt(data, options["rsa_public_key"])
            headers["x-culqi-rsa-id"] = options["rsa_id"]
            if "headers" in options:
                options["headers"].update(headers)
            else:
                options["headers"] = headers
            del options["rsa_public_key"]
            del options["rsa_id"]

        url = self._get_url(id_, "capture")
        return self._post(url, data, **options)

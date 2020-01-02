from .errors import (
    BadRequestError,
    ErrorCode,
    ErrorMessage,
    GatewayError,
    HTTPErrorCode,
    NotAllowedError,
    ServerError,
)
from .status_codes import HTTPStatusCode
from .urls import URL


def capitalize_camel_case(string):
    return "".join([item.capitalize() for item in string.split("_")])

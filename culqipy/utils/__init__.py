from .urls import URL
from .status_codes import HTTPStatusCode
from .errors import (
    ErrorCode,
    HTTPErrorCode,
    ErrorMessage,
    BadRequestError,
    GatewayError,
    ServerError,
    NotAllowedError
)


def capitalize_camel_case(string):
    return "".join([item.capitalize() for item in string.split('_')])

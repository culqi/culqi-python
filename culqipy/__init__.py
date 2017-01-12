# Configuration variables

API_URL = "https://api.culqi.com/v2"
COD_COMMERCE = None
API_KEY = None

# Resource

from culqipy.resource import (
    Token,
    Charge,
    Plan,
    Subscription,
    Refund
)

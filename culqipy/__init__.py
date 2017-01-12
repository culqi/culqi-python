# Configuration variables

API_URL = "https://api.culqi.com/v2"
COD_COMMERCE = None
API_KEY = None

# Resource

from culqipy import token
from culqipy import charge
from culqipy import plan
from culqipy import subscription
from culqipy import refund

Token = token.Token()
Charge = charge.Charge()
Plan = plan.Plan()
Subscription = subscription.Subscription()
Refund = refund.Refund()

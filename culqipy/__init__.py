# Configuration variables

API_URL = "https://api.culqi.com/v2"
COD_COMMERCE = None
API_KEY = None

# Resource

from culqipy import token
from charge import charge
from plan import plan
from subscription import subscription
from refund import refund

Token = token.Token()
Charge = charge.Charge()
Plan = plan.Plan()
Subscription = subscription.Subscription()
Refund = refund.Refund()

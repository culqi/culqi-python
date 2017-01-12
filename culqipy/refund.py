import culqipy, json, util
from object import Object

class Refund:

    def create(self, amount, charge_id, reason):
        refund = Object()
        refund.amount = amount
        refund.charge_id = charge_id
        refund.reason = reason
        return util.jsonResult(culqipy.API_KEY, "/refunds/", refund.toJSON(), "POST")

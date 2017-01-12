import culqipy, json, util
from object import Object

class Plan:

    def create(self, alias, amount, currency_code, interval, interval_count, limit, name, trial_days):
        plan = Object()
        plan.alias = alias
        plan.amount = amount
        plan.currency_code = currency_code
        plan.interval = interval
        plan.interval_count = interval_count
        plan.limit = limit
        plan.name = name
        plan.trial_days = trial_days
        return util.jsonResult(culqipy.API_KEY, "/plans/", plan.toJSON(), "POST")

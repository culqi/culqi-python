import culqipy
import unittest
import os

culqipy.secret_key = os.environ['LLAVE_SECRETA']


class ListTestStringMethods(unittest.TestCase):
    def test_list_tokens(self):
        params = {'iin': '411111'}
        data = False
        if len(culqipy.Token.list(params)['data']) >= 0:
            data = True
        self.assertTrue(data)

    def test_list_charges(self):
        params = {'min_amount': 500, 'max_amount': 1000}
        data = False
        if len(culqipy.Charge.list(params)['data']) >= 0:
            data = True
        self.assertTrue(data)

    def test_list_plans(self):
        data = False
        if len(culqipy.Plan.list(None)['data']) >= 0:
            data = True
        self.assertTrue(data)

    def test_list_events(self):
        data = False
        if len(culqipy.Event.list(None)['data']) >= 0:
            data = True
        self.assertTrue(data)

    def test_list_transfers(self):
        data = False
        if len(culqipy.Transfer.list(None)['data']) >= 0:
            data = True
        self.assertTrue(data)

    def test_list_subscriptions(self):
        data = False
        if len(culqipy.Subscription.list(None)['data']) >= 0:
            data = True
        self.assertTrue(data)

    def test_list_customers(self):
        data = False
        if len(culqipy.Customer.list(None)['data']) >= 0:
            data = True
        self.assertTrue(data)

    def test_list_cards(self):
        data = False
        if len(culqipy.Card.list(None)['data']) >= 0:
            data = True
        self.assertTrue(data)

    def test_list_refunds(self):
        data = False
        if len(culqipy.Refund.list(None)['data']) >= 0:
            data = True
        self.assertTrue(data)

if __name__ == '__main__':
    unittest.main()

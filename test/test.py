import culqipy
import unittest
import uuid
import os

culqipy.public_key = os.environ['LLAVE_PUBLICA']
culqipy.secret_key = os.environ['LLAVE_SECRETA']


class TestStringMethods(unittest.TestCase):

    @staticmethod
    def token(self):
        dir_token = {'card_number': '4111111111111111',
                     'cvv': '123',
                     'currency_code': 'PEN',
                     'email': 'wmuro@me.com',
                     'expiration_month': 9,
                     'expiration_year': 2020}

        return culqipy.Token.create(dir_token)

    @staticmethod
    def charge(self):
        dir_charge = {'amount': 1000,
                      'capture': True,
                      'currency_code': 'PEN',
                      'description': 'Venta de prueba',
                      'email': 'wmuro@me.com',
                      'installments': 0,
                      'metadata': {'test': '1234'},
                      'source_id': self.token(self)['id']}
        return culqipy.Charge.create(dir_charge)

    @staticmethod
    def plan(self):
        dir_plan = {'amount': 1000,
                    'currency_code': 'PEN',
                    'interval': 'dias',
                    'interval_count': 2,
                    'limit': 10,
                    'metadata': {'test': '1234'},
                    'name': 'plan-test-' + str(uuid.uuid1()),
                    'trial_days': 50}
        return culqipy.Plan.create(dir_plan)

    @staticmethod
    def customer(self):
        dir_customer = {'address': 'Avenida Lima 123213',
                        'address_city': 'LIMA',
                        'country_code': 'PE',
                        'email': 'wmuro'+str(uuid.uuid1())+'@me.com',
                        'first_name': 'William',
                        'last_name': 'Muro',
                        'metadata': {'other_email': 'wam@yahoo.com'},
                        'phone_number': 998989789,
                        }
        return culqipy.Customer.create(dir_customer)

    @staticmethod
    def card(self):
        dir_card = {
            'customer_id': self.customer(self)['id'],
            'token_id': self.token(self)['id'],
        }
        return culqipy.Card.create(dir_card)

    @staticmethod
    def subscription(self):
        dir_subscription = {'card_id': self.card(self)['id'],
                            'plan_id': self.plan(self)['id']}

        subscription = culqipy.Subscription.create(dir_subscription)
        return subscription

    @staticmethod
    def refund(self):
        dir_refund = {
            'amount': 500,
            'charge_id': self.charge(self)['id'],
            'reason': 'solicitud_comprador',
        }
        refund = culqipy.Refund.create(dir_refund)
        return refund

    def test_1_token(self):
        self.assertEqual('token', str(self.token(self)['object']))

    def test_2_charge(self):
        self.assertEqual('charge', str(self.charge(self)['object']))

    def test_3_charge_capture(self):
        capture_charge = culqipy.Charge.capture(self.charge(self)['id'])
        # The object of capture_charge is "error".
        self.assertNotEqual('charge', str(capture_charge['object']))

    def test_4_plan(self):
        self.assertEqual('plan', str(self.plan(self)['object']))

    def test_5_customer(self):
        self.assertEqual('customer', str(self.customer(self)['object']))

    def test_6_card(self):
        self.assertEqual('card', str(self.card(self)['object']))

    def test_7_subscription(self):
        self.assertEqual('subscription', str(self.subscription(self)['object']))

    def test_8_refund(self):
        self.assertEqual('refund', str(self.refund(self)['object']))

    # Find Resources

    def test_9_find_token(self):
        self.assertEqual('token', str(culqipy.Token.get(self.token(self)['id'])['object']))

    def test_10_find_charge(self):
        self.assertEqual('charge', str(culqipy.Charge.get(self.charge(self)['id'])['object']))

    def test_11_find_plan(self):
        self.assertEqual('plan', str(culqipy.Plan.get(self.plan(self)['id'])['object']))

    def test_12_find_customer(self):
        self.assertEqual('customer', str(culqipy.Customer.get(self.customer(self)['id'])['object']))

    def test_13_find_card(self):
        self.assertEqual('card', str(culqipy.Card.get(self.card(self)['id'])['object']))

    def test_14_find_subscription(self):
        self.assertEqual('subscription', str(culqipy.Subscription.get(self.subscription(self)['id'])['object']))

    def test_15_find_refund(self):
        self.assertEqual('refund', str(culqipy.Refund.get(self.refund(self)['id'])['object']))

    # Delete Resources

    def test_16_delete_subscription(self):
        self.assertTrue(culqipy.Subscription.delete(self.subscription(self)['id'])['deleted'])

    def test_17_delete_plan(self):
        self.assertTrue(culqipy.Plan.delete(self.plan(self)['id'])['deleted'])

    def test_18_delete_card(self):
        self.assertTrue(culqipy.Card.delete(self.card(self)['id'])['deleted'])

    def test_19_delete_customer(self):
        self.assertTrue(culqipy.Customer.delete(self.customer(self)['id'])['deleted'])


if __name__ == '__main__':
    unittest.main()

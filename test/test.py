import culqipy
import unittest
import uuid

culqipy.COD_COMMERCE = 'pk_test_vzMuTHoueOMlgUPj'
culqipy.API_KEY = 'sk_test_UTCQSGcXW8bCyU59'


class TestStringMethods(unittest.TestCase):
    def token(self):

        dir_token = {'card_number': '4111111111111111',
                     'cvv': '123',
                     'currency_code': 'PEN',
                     'email': 'wmuro@me.com',
                     'expiration_month': 9,
                     'expiration_year': 2020}

        return culqipy.Token.create(dir_token)

    def charge(self):
        dir_charge = {'amount': 1000,
                      'capture': True,
                      'currency_code': 'PEN',
                      'description': 'Venta de prueba',
                      'email': 'wmuro@me.com',
                      'installments': 0,
                      'metadata': {'test': '1234'},
                      'source_id': self.token()["id"]}
        return culqipy.Charge.create(dir_charge)

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

    def card(self):
        dir_card = {'customer_id': self.customer()["id"],
                   'token_id': self.token()["id"]}
        return culqipy.Card.create(dir_card)


    def subscription(self):
        dir_subscription = {'card_id': self.card()["id"],
                            'plan_id': self.plan()["id"]}

        subscription = culqipy.Subscription.create(dir_subscription)
        return subscription

    #def refund(self):
    #    dir_refund = {'amount': 500, 'charge_id': self.charge()["id"], 'reason': 'give me money back'}
    #    refund = culqipy.Refund.create(dir_refund)
    #    return refund

    def test_0_list_charge(self):
        params = {'iin': '411111'}
        token_list = culqipy.Token.list(params)
        data = False
        if len(token_list) > 0:
            data = True
        self.assertTrue(data)


    def test_1_token(self):
        self.assertEqual("token", str(self.token()["object"]))

    def test_2_find_token(self):
        id = self.token()["id"]
        token = culqipy.Token.get(id)
        self.assertEqual("token", str(token["object"]))

    def test_3_charge(self):
        self.assertEqual("charge", str(self.charge()["object"]))

    def test_4_charge_capture(self):
        capture_charge = culqipy.Charge.capture( str(self.charge()["id"]) )
        self.assertNotEqual("charge", str(capture_charge["object"]))

    def test_5_list_charge(self):
        params = {'min_amount': 500, 'max_amount': 1000}
        charge_list = culqipy.Charge.list(params)
        data = False
        if len(charge_list) > 0:
            data = True
        self.assertTrue(data)

    def test_6_plan(self):
        self.assertEqual("plan", str(self.plan()["object"]))

    def test_7_customer(self):
        self.assertEqual("customer", str(self.customer()["object"]))

    def test_8_card(self):
        self.assertEqual("card", str(self.card()["object"]))

    def test_9_subscription(self):
        self.assertEqual("subscription", str(self.subscription()["object"]))

    #def test_refund(self):
    #   self.assertEqual("refund", str(self.refund()["object"]))


if __name__ == '__main__':
    unittest.main()

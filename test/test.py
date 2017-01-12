import culqipy, unittest ,json, uuid

culqipy.COD_COMMERCE = "pk_test_vzMuTHoueOMlgUPj"
culqipy.API_KEY = "sk_test_UTCQSGcXW8bCyU59"

class TestStringMethods(unittest.TestCase):

    def token(self):
        token = culqipy.Token.create(
            card_number="4111111111111111",
            currency_code="PEN",
            cvv="123",
            exp_month=9,
            exp_year=2020,
            fingerprint="q352454534",
            last_name="Muro",
            email="wmuro@me.com",
            first_name="William")
        return token

    def charge(self):
        charge = culqipy.Charge.create(
            address="Avenida Lima 1232",
            address_city="LIMA",
            amount=1000,
            country_code="PE",
            currency_code="PEN",
            email="wmuro@me.com",
            first_name="William",
            installments=0,
            last_name="Muro",
            metadata="",
            phone_number=3333339,
            product_description="Venta de prueba",
            token_id=self.token()["id"])
        return charge

    def plan(self):
        plan = culqipy.Plan.create(
            alias="plan-test-"+str(uuid.uuid1()),
            amount=1000,
            currency_code="PEN",
            interval="day",
            interval_count=2,
            limit=10,
            name="Plan de Prueba "+str(uuid.uuid1()),
            trial_days=50)
        return plan

    def subscription(self):
        subscription = culqipy.Subscription.create(
            address="Avenida Lima 123213",
            address_city="LIMA",
            country_code="PE",
            email="wmuro@me.com",
            last_name="Muro",
            first_name="William",
            phone_number=1234567789,
            plan_alias=self.plan()["alias"],
            token_id=self.token()["id"])
        return subscription

    def refund(self):
        refund = culqipy.Refund.create(
            amount=500,
            charge_id=self.charge()["id"],
            reason="give me money back")
        return refund

    def test_token(self):
        self.assertEqual("token", str(self.token()["object"]))

    def test_charge(self):
        self.assertEqual("charge", str(self.charge()["object"]))

    def test_plan(self):
        self.assertEqual("plan", str(self.plan()["object"]))

    def test_subscription(self):
        self.assertEqual("subscription", str(self.subscription()["object"]))

    def test_refund(self):
        self.assertEqual("refund", str(self.refund()["object"]))

if __name__ == '__main__':
    unittest.main()

import unittest ,json, uuid
from culqi import Culqi

culqi  = Culqi("pk_test_vzMuTHoueOMlgUPj","sk_test_UTCQSGcXW8bCyU59")

class TestStringMethods(unittest.TestCase):

    culqi = Culqi("pk_test_vzMuTHoueOMlgUPj","sk_test_UTCQSGcXW8bCyU59")

    def token(self):
        token = culqi.createToken("4111111111111111","PEN","123",9,2020,"q352454534","Muro","wmuro@me.com","William")
        return token

    def charge(self):
        charge = culqi.createCharge("Avenida Lima 1232","LIMA",1000,"PE","PEN","wmuro@me.com","William",0,"Muro","",
                 9899,3333339,"Venta de prueba",self.token()["id"])
        return charge

    def plan(self):
        plan = culqi.createPlan("plan-test-"+str(uuid.uuid1()),1000,"PEN","day",2,10,"Plan de Prueba "+str(uuid.uuid1()),50)
        return plan

    def subscription(self):
        subscription = culqi.createSubscription("Avenida Lima 123213","LIMA","PE","wmuro@me.com","Muro","William",
                       1234567789,self.plan()["alias"],self.token()["id"])
        return subscription

    def refund(self):
        refund = culqi.createRefund(500,self.charge()["id"],"give me money back")
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

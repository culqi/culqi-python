import json
from culqi import Culqi

def main():
    culqi = Culqi("pk_test_vzMuTHoueOMlgUPj","sk_test_UTCQSGcXW8bCyU59")
    token = json.loads(culqi.createToken(
            "4111111111111111","PEN","123",9,2020,"q352454534","Muro","wmuro@me.com","William"
            ))

    print token["id"]

    charge = json.loads(culqi.createCharge("Avenida Lima 1232","LIMA",1000,"PE","PEN","wmuro@me.com","William",0,"Muro","",
             9899,3333339,"Venta de prueba",token["id"]))
    print charge["id"]

    plan = json.loads(culqi.createPlan("plan-test-CULQI117",1000,"PEN","day",2,10,"Plan de Prueba CULQI117",50))
    print plan["alias"]

    subscription = json.loads(culqi.createSubscription("Avenida Lima 123213","LIMA","PE","wmuro@me.com","Muro","William",
                   1234567789,plan["alias"],token["id"]))
    print subscription

    refund = json.loads(culqi.createRefund(500,charge["id"],"give me money back"))
    print refund

if __name__ == "__main__":
    main()

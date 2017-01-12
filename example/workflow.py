import uuid
import culqipy

def main():

    culqipy.COD_COMMERCE = "pk_test_vzMuTHoueOMlgUPj"
    culqipy.API_KEY = "sk_test_UTCQSGcXW8bCyU59"

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

    print(token["id"])

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
        token_id=token["id"])

    print(charge["id"])

    plan = culqipy.Plan.create(
        alias="plan-test-"+str(uuid.uuid1()),
        amount=1000,
        currency_code="PEN",
        interval="day",
        interval_count=2,
        limit=10,
        name="Plan de Prueba "+str(uuid.uuid1()),
        trial_days=50)

    print(plan["alias"])

    subscription = culqipy.Subscription.create(
        address="Avenida Lima 123213",
        address_city="LIMA",
        country_code="PE",
        email="wmuro@me.com",
        last_name="Muro",
        first_name="William",
        phone_number=1234567789,
        plan_alias=plan["alias"],
        token_id=token["id"])

    print(subscription)

    refund = culqipy.Refund.create(
        amount=500,
        charge_id=charge["id"],
        reason="give me money back")

    print(refund)

if __name__ == "__main__":
    main()

import uuid
import culqipy
import os


def main():
    culqipy.public_key = os.environ['LLAVE_PUBLICA']
    culqipy.secret_key = os.environ['LLAVE_SECRETA']

    # CREATE TOKEN

    dir_token = {'card_number': '4111111111111111',
                 'cvv': '123',
                 'currency_code': 'PEN',
                 'email': 'wmuro@me.com',
                 'expiration_month': 9,
                 'expiration_year': 2020}

    token = culqipy.Token.create(dir_token)

    print(token['id'])

    # CREATE CHARGE

    dir_charge = {'amount': 1000,
                  'capture': True,
                  'currency_code': 'PEN',
                  'description': 'Venta de prueba',
                  'email': 'wmuro@me.com',
                  'installments': 0,
                  'metadata': {'test': '1234'},
                  'source_id': token['id']}

    charge = culqipy.Charge.create(dir_charge)

    print(charge['id'])

    # CREATE PLAN

    dir_plan = {'amount': 1000,
                'currency_code': 'PEN',
                'interval': 'dias',
                'interval_count': 2,
                'limit': 10,
                'metadata': {'test': '1234'},
                'name': 'plan-test-' + str(uuid.uuid1()),
                'trial_days': 50}

    plan = culqipy.Plan.create(dir_plan)

    print(plan['id'])

    # CREATE CUSTOMER

    dir_customer = {'address': 'Avenida Lima 123213',
                    'address_city': 'LIMA',
                    'country_code': 'PE',
                    'email': 'wmuro' + str(uuid.uuid1()) + '@me.com',
                    'first_name': 'William',
                    'last_name': 'Muro',
                    'metadata': {'other_email': 'wam@yahoo.com'},
                    'phone_number': 998989789,
                    }

    customer = culqipy.Customer.create(dir_customer)

    print(customer['id'])

    # CREATE CARD

    dir_token = {'card_number': '4111111111111111',
                 'cvv': '123',
                 'currency_code': 'PEN',
                 'email': 'wmuro@me.com',
                 'expiration_month': 9,
                 'expiration_year': 2020}

    token_for_card = culqipy.Token.create(dir_token)

    dir_card = {'customer_id': customer['id'],
                'token_id': token_for_card['id']}

    card = culqipy.Card.create(dir_card)

    print(card['id'])

    # CREATE SUBSCRIPTION

    dir_subscription = {'card_id': card['id'],
                        'plan_id': plan['id']}

    subscription = culqipy.Subscription.create(dir_subscription)

    print(subscription['id'])

    # CREATE REFUNDS

    dir_refund = {'amount': 500, 'charge_id': charge['id'], 'reason': 'solicitud_comprador'}

    refund = culqipy.Refund.create(dir_refund)

    print(refund['id'])

if __name__ == "__main__":
    main()

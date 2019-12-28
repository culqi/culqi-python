# Culqi Python

![GitHub](https://img.shields.io/github/license/culqi/culqi-python.svg?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/culqipy.svg?style=for-the-badge)
![Travis (.org) branch](https://img.shields.io/travis/culqi/culqi-python/master.svg?style=for-the-badge)

Biblioteca de CULQI para el lenguaje Python, pagos simples en tu sitio web. Consume el Culqi API.

| Versión actual     | Culqi API                      |
| ------------------ | ------------------------------ |
| 0.2.6 (2017-02-27) | [v2](https://culqi.com/api/#/) |

## Requisitos

- Python 2.7, 3.5, 3.6, 3.7, 3.8-dev
- Credenciales de comercio en Culqi (1).

## Instalación

```bash
pip install culqipy
```

## Ejemplo

#### Imports

```python
from uuid import uuid4
import culqipy
```

#### Inicialización

```python
api_key = '{LLAVE PUBLICA}'
api_secret = '{LLAVE SECRETA}'

client = Client(api_key=api_key, api_secret=api_secret)
```

#### Token

##### Create

```python
token_data = {
      "cvv": "123",
      "card_number": "4111111111111111",
      "expiration_year": "2020",
      "expiration_month": "09",
      "email": "richard@piedpiper.com",
}

token = client.token.create(data=token_data)
print(token["data"])
```

##### Read

```python
retrieved_token = self.token.read(token["data"]["id"])
print(retrieved_token["data"])
```

##### Update

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_token = self.token.update(id_=token["data"]["id"], data=metadatada)
print(updated_token["data"])
```

##### List

```python
retrieved_token_list = self.token.list()
assert "items" in retrieved_token_list["data"]
```

#### Charge

##### Create

```python
charge_data = {
      "amount": 10000,
      "capture": False,
      "currency_code": "PEN",
      "description": "Venta de prueba",
      "email": "richard@piedpiper.com",
      "installments": 0,
      "source_id": token["data"]["id"],
}

charge = client.charge.create(data=charge_data)
print(charge["data"])
```

##### Capture

```python
captured_charge = self.charge.capture(charge["data"]["id"])
print(captured_charge["data"])
```

##### Read

```python
retrieved_charge = self.charge.read(charge["data"]["id"])
print(retrieved_charge["data"])
```

##### Update

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_charge = self.charge.update(id_=charge["data"]["id"], data=metadatada)
print(updated_charge["data"])
```

##### List

```python
retrieved_charge_list = self.charge.list()
assert "items" in retrieved_charge_list["data"]
```

#### Refund

##### Create

```python
refund_data = {
      "amount": 100,
      "reason": "solicitud_comprador",
      "charge_id": charge["data"]["id"],
}

refund = client.refund.create(data=refund_data)
print(refund["data"])
```

##### Read

```python
retrieved_refund = self.refund.read(refund["data"]["id"])
print(retrieved_refund["data"])
```

##### Update

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_refund = self.refund.update(id_=refund["data"]["id"], data=metadatada)
print(updated_refund["data"])
```

##### List

```python
retrieved_refund_list = self.refund.list()
assert "items" in retrieved_refund_list["data"]
```

#### Customer

##### Create

```python
customer_data = {
      "address": "Avenida Lima 123213",
      "address_city": "LIMA",
      "country_code": "PE",
      "email": "richard@piedpiper.com",
      "first_name": "Richard",
      "last_name": "Piedpiper",
      "phone_number": "+51998989789",
}

customer = client.customer.create(data=customer_data)
print(customer["data"])
```

##### Read

```python
retrieved_customer = self.customer.read(customer["data"]["id"])
print(retrieved_customer["data"])
```

##### Update

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_customer = self.customer.update(id_=customer["data"]["id"], data=metadatada)
print(updated_customer["data"])
```

##### Delete

```python
deleted_customer = self.customer.delete(id_=customer["data"]["id"])
print(deleted_customer["data"])
```

##### List

```python
retrieved_customer_list = self.customer.list()
assert "items" in retrieved_customer_list["data"]
```

#### Card

##### Create

```python
card_data = {
      "token_id": token["data"]["id"],
      "customer_id": customer["data"]["id"],
}

card = client.card.create(data=card_data)
print(card["data"])
```

##### Read

```python
retrieved_card = self.card.read(card["data"]["id"])
print(retrieved_card["data"])
```

##### Update

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_card = self.card.update(id_=card["data"]["id"], data=metadatada)
print(updated_card["data"])
```

##### Delete

```python
deleted_card = self.card.delete(id_=card["data"]["id"])
print(deleted_card["data"])
```

##### List

```python
retrieved_card_list = self.card.list()
assert "items" in retrieved_card_list["data"]
```

#### Plan

##### Create

```python
plan_data = {
      "amount": 1000,
      "currency_code": "PEN",
      "interval": "dias",
      "interval_count": 2,
      "limit": 10,
      "name": "plan-{0}".format(uuid4().hex[:4]),
      "trial_days": 30,
}

plan = client.plan.create(data=plan_data)
print(plan["data"])
```

##### Read

```python
retrieved_plan = self.plan.read(plan["data"]["id"])
print(retrieved_plan["data"])
```

##### Update

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_plan = self.plan.update(id_=plan["data"]["id"], data=metadatada)
print(updated_plan["data"])
```

##### Delete

```python
deleted_plan = self.plan.delete(id_=plan["data"]["id"])
print(deleted_plan["data"])
```

##### List

```python
retrieved_plan_list = self.plan.list()
assert "items" in retrieved_plan_list["data"]
```

#### Subscription

##### Create

```python
subscription_data = {
      "card_id": card["data"]["id"],
      "plan_id": plan["data"]["id"],
}

subscription = client.subscription.create(data=subscription_data)
print(subscription["data"])
```

##### Read

```python
retrieved_subscription = self.subscription.read(subscription["data"]["id"])
print(retrieved_subscription["data"])
```

##### Update

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_subscription = self.subscription.update(id_=subscription["data"]["id"], data=metadatada)
print(updated_subscription["data"])
```

##### Delete

```python
deleted_subscription = self.subscription.delete(id_=subscription["data"]["id"])
print(deleted_subscription["data"])
```

##### List

```python
retrieved_subscription_list = self.subscription.list()
assert "items" in retrieved_subscription_list["data"]
```

#### Order

##### Create

```python
order_data = {
      "amount": 1000,
      "currency_code": "PEN",
      "description": "Venta de prueba",
      "order_number": "order-{0}".format(uuid4().hex[:4]),
      "client_details": {
            "first_name": "Richard",
            "last_name": "Piedpiper",
            "email": "richard@piedpiper.com",
            "phone_number": "+51998989789",
      },
      "expiration_date": 1893474000,
      "confirm": False,
}

order = client.order.create(data=order_data)
print(order["data"])
```

##### Confirm

```python
confirmed_order = self.order.confirm(order["data"]["id"])
print(confirmed_order["data"])
```

##### Read

```python
retrieved_order = self.order.read(order["data"]["id"])
print(retrieved_order["data"])
```

##### Update

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_order = self.order.update(id_=order["data"]["id"], data=metadatada)
print(updated_order["data"])
```

##### Delete

```python
deleted_order = self.order.delete(order["data"]["id"])
print(deleted_order["data"])
```

##### List

```python
retrieved_order_list = self.order.list()
assert "items" in retrieved_order_list["data"]
```

#### Event

##### Read

```python
retrieved_event = self.event.read(event_id)
print(retrieved_event["data"])
```

##### List

```python
retrieved_event_list = self.event.list()
assert "items" in retrieved_event_list["data"]
```

#### Iin

##### Read

```python
retrieved_iin = self.iin.read(iin_id)
print(retrieved_iin["data"])
```

##### List

```python
retrieved_iin_list = self.iin.list()
assert "items" in retrieved_iin_list["data"]
```

#### Transfer

```python
retrieved_transfer = self.transfer.read(transfer_id)
print(retrieved_transfer["data"])
```

##### List

```python
retrieved_transfer_list = self.transfer.list()
assert "items" in retrieved_transfer_list["data"]
```

#### Nota

Cada metodo retona un diccionario con la estructura

```python
{
      "status": status_code,
      "data": data
}
```

El `status_code` es el estatus HTTP numérico devuelto por la solicitud HTTP que se
realiza al API de Culqi, y `data` contiene el cuerpo de la respuesta obtenida.

## Documentación

- ¿Necesitas más información para integrar Culqi?

  La documentación completa se encuentra en [https://culqi.com/docs/](https://culqi.com/docs/)

- Quieres saber mas de nuestra API

  Encuentra lo que necesitas en [https://www.culqi.com/api/](https://www.culqi.com/api/)

## Changelog

Todos los cambios en las versiones de esta biblioteca están listados en
[CHANGELOG.md](CHANGELOG.md).

## Desarrollo

Si estas interesado en contribuir con el desarrollo y mantenimiento de este paquete
es recomendable que emplees [poetry](https://poetry.eustace.io) para la gestión de dependencias.

#### Entorno

Clona el proyecto

```bash
$ git clone https://github.com/culqi/culqi-python.git
$ cd culqi-python
```

Instala las dependencias

```bash
$ poetry install
```

#### Testing and coverage

Puedes ejecutar los tests con poetry

```bash
poetry run pytest --cov --cov-report=
poetry run coverage report
```

#### ¿Quieres enviar un PR?

Antes de hacer tu primer commit y enviar tu pull request ejecuta

```bash
$ poetry run pre-commit install
```

Y relaiza tu commits de forma habitual.

## Autor

Willy Aguirre ([@marti1125](https://github.com/marti1125) - Team Culqi)

Nuestros [Contribuidores](https://github.com/culqi/culqi-python/graphs/contributors)

## Licencia

El código fuente de culqi-python está distribuido bajo MIT License, revisar el archivo [LICENSE](https://github.com/culqi/culqi-python/blob/master/LICENSE.txt).

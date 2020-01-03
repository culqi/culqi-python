# Culqi Python

![GitHub](https://img.shields.io/github/license/culqi/culqi.svg?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/culqi.svg?style=for-the-badge)
![Travis (.org) branch](https://img.shields.io/travis/culqi/culqi/master.svg?style=for-the-badge)

Biblioteca de CULQI para el lenguaje Python, pagos simples en tu sitio web. Consume el Culqi API.

| Versión actual     | Culqi API                    |
| ------------------ | ---------------------------- |
| 0.2.6 (2017-02-27) | [v2](https://culqi.com/api/) |

## Requisitos

- Python 2.7, 3.5, 3.6, 3.7, 3.8-dev
- Credenciales de comercio en [Culqi](https://culqi.com).

## Instalación

```bash
pip install culqi
```

## Ejemplo

#### Inicialización

```python
from uuid import uuid4
import culqi

public_key = '{LLAVE PUBLICA}'
private_key = '{LLAVE SECRETA}'

client = Client(public_key=public_key, private_key=private_key)
```

#### Token

##### Crear

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

##### Leer

```python
retrieved_token = client.token.read(token["data"]["id"])
print(retrieved_token["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_token = client.token.update(id_=token["data"]["id"], data=metadatada)
print(updated_token["data"])
```

##### Listar

```python
retrieved_token_list = client.token.list()
assert "items" in retrieved_token_list["data"]
```

#### Cargo

##### Crear

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

##### Capturar

```python
captured_charge = client.charge.capture(charge["data"]["id"])
print(captured_charge["data"])
```

##### Leer

```python
retrieved_charge = client.charge.read(charge["data"]["id"])
print(retrieved_charge["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_charge = client.charge.update(id_=charge["data"]["id"], data=metadatada)
print(updated_charge["data"])
```

##### Listar

```python
retrieved_charge_list = client.charge.list()
assert "items" in retrieved_charge_list["data"]
```

#### Reembolso

##### Crear

```python
refund_data = {
      "amount": 100,
      "reason": "solicitud_comprador",
      "charge_id": charge["data"]["id"],
}

refund = client.refund.create(data=refund_data)
print(refund["data"])
```

##### Leer

```python
retrieved_refund = client.refund.read(refund["data"]["id"])
print(retrieved_refund["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_refund = client.refund.update(id_=refund["data"]["id"], data=metadatada)
print(updated_refund["data"])
```

##### Listar

```python
retrieved_refund_list = client.refund.list()
assert "items" in retrieved_refund_list["data"]
```

#### Cliente

##### Crear

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

##### Leer

```python
retrieved_customer = client.customer.read(customer["data"]["id"])
print(retrieved_customer["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_customer = client.customer.update(id_=customer["data"]["id"], data=metadatada)
print(updated_customer["data"])
```

##### Eliminar

```python
deleted_customer = client.customer.delete(id_=customer["data"]["id"])
print(deleted_customer["data"])
```

##### Listar

```python
retrieved_customer_list = client.customer.list()
assert "items" in retrieved_customer_list["data"]
```

#### Tarjeta

##### Crear

```python
card_data = {
      "token_id": token["data"]["id"],
      "customer_id": customer["data"]["id"],
}

card = client.card.create(data=card_data)
print(card["data"])
```

##### Leer

```python
retrieved_card = client.card.read(card["data"]["id"])
print(retrieved_card["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_card = client.card.update(id_=card["data"]["id"], data=metadatada)
print(updated_card["data"])
```

##### Eliminar

```python
deleted_card = client.card.delete(id_=card["data"]["id"])
print(deleted_card["data"])
```

##### Listar

```python
retrieved_card_list = client.card.list()
assert "items" in retrieved_card_list["data"]
```

#### Plan

##### Crear

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

##### Leer

```python
retrieved_plan = client.plan.read(plan["data"]["id"])
print(retrieved_plan["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_plan = client.plan.update(id_=plan["data"]["id"], data=metadatada)
print(updated_plan["data"])
```

##### Eliminar

```python
deleted_plan = client.plan.delete(id_=plan["data"]["id"])
print(deleted_plan["data"])
```

##### Listar

```python
retrieved_plan_list = client.plan.list()
assert "items" in retrieved_plan_list["data"]
```

#### Suscripción

##### Crear

```python
subscription_data = {
      "card_id": card["data"]["id"],
      "plan_id": plan["data"]["id"],
}

subscription = client.subscription.create(data=subscription_data)
print(subscription["data"])
```

##### Leer

```python
retrieved_subscription = client.subscription.read(subscription["data"]["id"])
print(retrieved_subscription["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_subscription = client.subscription.update(id_=subscription["data"]["id"], data=metadatada)
print(updated_subscription["data"])
```

##### Eliminar

```python
deleted_subscription = client.subscription.delete(id_=subscription["data"]["id"])
print(deleted_subscription["data"])
```

##### Listar

```python
retrieved_subscription_list = client.subscription.list()
assert "items" in retrieved_subscription_list["data"]
```

#### Orden

##### Crear

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

##### Confirmar

```python
confirmed_order = client.order.confirm(order["data"]["id"])
print(confirmed_order["data"])
```

##### Leer

```python
retrieved_order = client.order.read(order["data"]["id"])
print(retrieved_order["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
updated_order = client.order.update(id_=order["data"]["id"], data=metadatada)
print(updated_order["data"])
```

##### Eliminar

```python
deleted_order = client.order.delete(order["data"]["id"])
print(deleted_order["data"])
```

##### Listar

```python
retrieved_order_list = client.order.list()
assert "items" in retrieved_order_list["data"]
```

#### Evento

##### Leer

```python
retrieved_event = client.event.read(event_id)
print(retrieved_event["data"])
```

##### Listar

```python
retrieved_event_list = client.event.list()
assert "items" in retrieved_event_list["data"]
```

#### Iin

##### Leer

```python
retrieved_iin = client.iin.read(iin_id)
print(retrieved_iin["data"])
```

##### Listar

```python
retrieved_iin_list = client.iin.list()
assert "items" in retrieved_iin_list["data"]
```

#### Transferencia

##### Leer

```python
retrieved_transfer = client.transfer.read(transfer_id)
print(retrieved_transfer["data"])
```

##### Listar

```python
retrieved_transfer_list = client.transfer.list()
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

- Quieres saber más de nuestra API

  Encuentra lo que necesitas en [https://www.culqi.com/api/](https://www.culqi.com/api/)

## Changelog

Todos los cambios en las versiones de esta biblioteca están listados en
[CHANGELOG.md](CHANGELOG.md).

## Desarrollo

Si estas interesado en contribuir con el desarrollo y mantenimiento de este paquete
es recomendable que emplees [poetry](https://poetry.eustace.io) para la gestión de
dependencias.

#### Entorno

Clona el proyecto

```bash
$ git clone https://github.com/culqi/culqi.git
$ cd culqi
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

Luego relaiza tu commits de forma habitual.

## Autor

Willy Aguirre ([@marti1125](https://github.com/marti1125) - Team Culqi)

Nuestros [Contribuidores](https://github.com/culqi/culqi/graphs/contributors)

## Licencia

El código fuente de `culqi` está distribuido bajo MIT License, revisar el archivo
[LICENSE.txt](LICENSE.txt).

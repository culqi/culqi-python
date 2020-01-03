# Culqi Python


[![Build Status](https://travis-ci.org/culqi/culqi-python.svg?branch=master)](https://travis-ci.org/culqi/culqi-python)


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
import culqi

public_key = '{LLAVE PUBLICA}'
private_key = '{LLAVE SECRETA}'

culqi = Culqi(public_key=public_key, private_key=private_key)
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

response = client.token.create(data=token_data)
print(response["data"])
```

##### Leer

```python
response = client.token.read(token["data"]["id"])
print(response["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
response = client.token.update(id_=token["data"]["id"], data=metadatada)
print(response["data"])
```

##### Listar

```python
response = client.token.list()
assert "items" in response["data"]
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

response = client.charge.create(data=charge_data)
print(response["data"])
```

##### Capturar

```python
response = client.charge.capture(charge["data"]["id"])
print(response["data"])
```

##### Leer

```python
response = client.charge.read(charge["data"]["id"])
print(response["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
response = client.charge.update(id_=charge["data"]["id"], data=metadatada)
print(response["data"])
```

##### Listar

```python
response = client.charge.list()
assert "items" in response["data"]
```

#### Reembolso

##### Crear

```python
refund_data = {
      "amount": 100,
      "reason": "solicitud_comprador",
      "charge_id": charge["data"]["id"],
}

response = client.refund.create(data=refund_data)
print(response["data"])
```

##### Leer

```python
response = client.refund.read(refund["data"]["id"])
print(response["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
response = client.refund.update(id_=refund["data"]["id"], data=metadatada)
print(response["data"])
```

##### Listar

```python
response = client.refund.list()
assert "items" in response["data"]
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

response = client.customer.create(data=customer_data)
print(response["data"])
```

##### Leer

```python
response = client.customer.read(customer["data"]["id"])
print(response["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
response = client.customer.update(id_=customer["data"]["id"], data=metadatada)
print(response["data"])
```

##### Eliminar

```python
response = client.customer.delete(id_=customer["data"]["id"])
print(response["data"])
```

##### Listar

```python
response = client.customer.list()
assert "items" in response["data"]
```

#### Tarjeta

##### Crear

```python
card_data = {
      "token_id": token["data"]["id"],
      "customer_id": customer["data"]["id"],
}

response = client.card.create(data=card_data)
print(response["data"])
```

##### Leer

```python
response = client.card.read(card["data"]["id"])
print(response["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
response = client.card.update(id_=card["data"]["id"], data=metadatada)
print(response["data"])
```

##### Eliminar

```python
response = client.card.delete(id_=card["data"]["id"])
print(response["data"])
```

##### Listar

```python
response = client.card.list()
assert "items" in response["data"]
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

response = client.plan.create(data=plan_data)
print(response["data"])
```

##### Leer

```python
response = client.plan.read(plan["data"]["id"])
print(response["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
response = client.plan.update(id_=plan["data"]["id"], data=metadatada)
print(response["data"])
```

##### Eliminar

```python
response = client.plan.delete(id_=plan["data"]["id"])
print(response["data"])
```

##### Listar

```python
response = client.plan.list()
assert "items" in response["data"]
```

#### Suscripción

##### Crear

```python
subscription_data = {
      "card_id": card["data"]["id"],
      "plan_id": plan["data"]["id"],
}

response = client.subscription.create(data=subscription_data)
print(response["data"])
```

##### Leer

```python
response = client.subscription.read(subscription["data"]["id"])
print(response["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
response = client.subscription.update(id_=subscription["data"]["id"], data=metadatada)
print(response["data"])
```

##### Eliminar

```python
response = client.subscription.delete(id_=subscription["data"]["id"])
print(response["data"])
```

##### Listar

```python
response = client.subscription.list()
assert "items" in response["data"]
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

response = client.order.create(data=order_data)
print(response["data"])
```

##### Confirmar

```python
response = client.order.confirm(order["data"]["id"])
print(response["data"])
```

##### Leer

```python
response = client.order.read(order["data"]["id"])
print(response["data"])
```

##### Actualizar

```python
metadatada = {
      "metadata": {
            "order_id": "0001"
      }
}
response = client.order.update(id_=order["data"]["id"], data=metadatada)
print(response["data"])
```

##### Eliminar

```python
response = client.order.delete(order["data"]["id"])
print(response["data"])
```

##### Listar

```python
response = client.order.list()
assert "items" in response["data"]
```

#### Evento

##### Leer

```python
response = client.event.read(event_id)
print(response["data"])
```

##### Listar

```python
response = client.event.list()
assert "items" in response["data"]
```

#### Iin

##### Leer

```python
response = client.iin.read(iin_id)
print(response["data"])
```

##### Listar

```python
response = client.iin.list()
assert "items" in response["data"]
```

#### Transferencia

##### Leer

```python
response = client.transfer.read(transfer_id)
print(response["data"])
```

##### Listar

```python
response = client.transfer.list()
assert "items" in response["data"]
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

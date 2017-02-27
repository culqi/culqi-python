# Culqi Python

[![License](https://poser.pugx.org/culqi/culqi-php/license)](https://github.com/culqi/culqi-python/blob/master/LICENSE.txt)
[![Latest Unstable Version](https://poser.pugx.org/culqi/culqi-php/v/unstable)](https://pypi.python.org/pypi/culqi_py)
[![Build Status](https://travis-ci.org/culqi/culqi-python.svg?branch=master)](https://travis-ci.org/culqi/culqi-python)

Biblioteca de CULQI para el lenguaje Python, pagos simples en tu sitio web. Consume el Culqi API.

| Versión actual|Culqi API|
|----|----|
| 0.2.6 (2017-02-27) |[v2](https://culqi.com/api/#/)|

## Requisitos

- Python 2.6, 2.7, 3.3, 3.4, 3.5, 3.6
- Credenciales de comercio en Culqi (1).

## Instalación

```bash
pip install culqipy
```

## Ejemplo

#### Imports

```python
# example.py
import uuid
import culqipy
```
#### Inicialización

```python
culqipy.public_key = '{LLAVE PUBLICA}'
culqipy.secret_key = '{LLAVE SECRETA}'
```

#### Crear Token

```python
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
```

#### Crear Cargo

```python
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
```

#### Crear Plan

```python
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
```

#### Crear Suscripción

```python
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
```

#### Crear Devolución

```python
refund = culqipy.Refund.create(
      amount=500,
      charge_id=charge["id"],
      reason="solicitud_comprador")

print(refund)
```
#### Nota
Cada metodo retona un objecto json y puede ser accedido de la siguiente forma jsonObject["key"]

## Documentación
¿Necesitas más información para integrar `culqi-python`? La documentación completa se encuentra en [https://culqi.com/docs/](https://culqi.com/docs/)

## Changelog

Todos los cambios en las versiones de esta biblioteca están listados en [CHANGELOG](CHANGELOG).

## Dependencias para el desarrollo

[requests](http://docs.python-requests.org/en/master/)

## Testing

Solo debe ejecutar el siguiente comando

```python
python culqipy/test.py
```

## Autor

Willy Aguirre ([@marti1125](https://github.com/marti1125) - Team Culqi)

Nuestros [Contribuidores](https://github.com/culqi/culqi-python/graphs/contributors)

## Licencia

El código fuente de culqi-python está distribuido bajo MIT License, revisar el archivo [LICENSE](https://github.com/culqi/culqi-python/blob/master/LICENSE.txt).

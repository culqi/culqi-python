# Culqi Python

[![License](https://poser.pugx.org/culqi/culqi-php/license)](https://github.com/culqi/culqi-python/blob/master/LICENSE.txt)
[![Latest Unstable Version](https://poser.pugx.org/culqi/culqi-php/v/unstable)](https://pypi.python.org/pypi/culqi_py)
[![Build Status](https://travis-ci.org/culqi/culqi-python.svg?branch=master)](https://travis-ci.org/culqi/culqi-python)

Biblioteca de CULQI para el lenguaje Python, pagos simples en tu sitio web. Consume el Culqi API.

| Versión actual|Culqi API|
|----|----|
| 0.1.0 (2017-01-09) |[v2](https://beta.culqi.com)|

## Requisitos

- Python 2.6, 2.7, 3.3, 3.4, 3.5
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
from culqipy import culqi
```
#### Inicialización
| Parametros | Tipo de dato |
|----|----|
| COD_COMMERCE | String |
| API_KEY | String |

```python
culqiObject = culqi.Culqi("pk_test_vzMuTHoueOMlgUPj","sk_test_UTCQSGcXW8bCyU59")
```

#### Crear Token
| Parametros | Tipo de dato |
|----|----|
| card_number | String |
| currency_code | String |
| cvv | String |
| expiration_month | int |
| expiration_year | int |
| fingerprint | String |
| last_name | String |
| email | String |
| first_name | String |

```python
token = culqiObject.createToken("4111111111111111","PEN","123",9,2020,"q352454534","Muro","wmuro@me.com","William")

print token["id"]
```

#### Crear Cargo
| Parametros | Tipo de dato |
|----|----|
| address | String |
| address_city | String |
| amount | int |
| country_code | String |
| currency_code | String |
| email | String |
| first_name | String |
| installments | int |
| last_name | String |
| metadata | String |
| phone_number | int |
| product_description | String |
| token_id | String |

```python
charge = culqiObject.createCharge("Avenida Lima 1232","LIMA",1000,"PE","PEN","wmuro@me.com","William",0,"Muro",""
        ,3333339,"Venta de prueba",token["id"])
print charge["id"]
```

#### Crear Plan
| Parametros | Tipo de dato |
|----|----|
| alias | String |
| amount | int |
| currency_code | String |
| interval | String |
| interval_count | int |
| limit | int |
| name | String |
| trial_days | int |

```python
plan = culqiObject.createPlan("plan-test-"+str(uuid.uuid1()),1000,"PEN","day",2,10,"Plan de Prueba"+str(uuid.uuid1()),50)
print plan["alias"]
```

#### Crear Suscripción
| Parametros | Tipo de dato |
|----|----|
| address | String |
| address_city | String |
| country_code | String |
| email | String |
| first_name | String |
| last_name | String |
| phone_number | int |
| plan_alias | String |
| token_id | String |

```python
subscription = culqiObject.createSubscription("Avenida Lima 123213","LIMA","PE","wmuro@me.com","Muro","William",1234567789,plan["alias"],token["id"])
print subscription
```

#### Crear Devolución
| Parametros | Tipo de dato |
|----|----|
| amount | int |
| charge_id | String |
| reason | String |

```python
refund = culqiObject.createRefund(500,charge["id"],"give me money back")
print refund
```
#### Nota
Cada metodo retona un objecto json y puede ser accedido de la siguiente forma jsonObject["key"]

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

## Licencia

El código fuente de culqi-python está distribuido bajo MIT License, revisar el archivo [LICENSE](https://github.com/culqi/culqi-python/blob/master/LICENSE.txt).

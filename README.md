# Culqi-Python

[![Build Status](https://travis-ci.org/culqi/culqi-python.svg?branch=master)](https://travis-ci.org/culqi/culqi-python)
![](https://img.shields.io/pypi/pyversions/Culqi)
![](https://img.shields.io/pypi/l/culqi)
![](https://img.shields.io/pypi/v/culqi)


Nuestra Biblioteca PYTHON oficial, es compatible con la v2.0 del Culqi API, con el cual tendrás la posibilidad de realizar cobros con tarjetas de débito y crédito, Yape, PagoEfectivo, billeteras móviles y Cuotéalo con solo unos simples pasos de configuración.

Nuestra biblioteca te da la posibilidad de capturar el `status_code` de la solicitud HTTP que se realiza al API de Culqi, así como el `response` que contiene el cuerpo de la respuesta obtenida.

## Requisitos

- Python 2.7+
* Afiliate [aquí](https://afiliate.culqi.com/).
* Si vas a realizar pruebas obtén tus llaves desde [aquí](https://integ-panel.culqi.com/#/registro), si vas a realizar transacciones reales obtén tus llaves desde [aquí](https://panel.culqi.com/#/registro).

> Recuerda que para obtener tus llaves debes ingresar a tu CulqiPanel > Desarrollo > ***API Keys***.

![alt tag](http://i.imgur.com/NhE6mS9.png)

> Recuerda que las credenciales son enviadas al correo que registraste en el proceso de afiliación.

* Para encriptar el payload debes generar un id y llave RSA  ingresando a CulqiPanel > Desarrollo  > RSA Keys

## Instalación

Ejecuta los siguientes comandos:

```bash
py -m pip install pytest
py -m pip install python-dotenv
py -m pip install culqi
py -m pip install jsonschema
py -m pip install pycryptodome

```

## Configuracion

Para empezar a enviar peticiones al API de Culqi debes configurar tu llave pública (pk), llave privada (sk).
Para habilitar encriptación de payload debes configurar tu rsa_id y rsa_public_key.

```python

from dotenv import load_dotenv
from culqi2 import __version__
from culqi2.client import Culqi

self.public_key = "pk_test_e94078b9b248675d"
self.private_key = "sk_test_c2267b5b262745f0"
self.culqi = Culqi(self.public_key, self.private_key)

#ecnrypt variables
self.rsa_public_key = "-----BEGIN PUBLIC KEY-----\n" + \
                        "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDswQycch0x/7GZ0oFojkWCYv+g\n" + \
                        "r5CyfBKXc3Izq+btIEMCrkDrIsz4Lnl5E3FSD7/htFn1oE84SaDKl5DgbNoev3pM\n" + \
                        "C7MDDgdCFrHODOp7aXwjG8NaiCbiymyBglXyEN28hLvgHpvZmAn6KFo0lMGuKnz8\n" + \
                        "iuTfpBl6HpD6+02SQIDAQAB\n" + \
                        "-----END PUBLIC KEY-----"
self.rsa_id = "de35e120-e297-4b96-97ef-10a43423ddec"

```

### Encriptar payload

Para encriptar el payload necesitas agregar el parámetros **options** que contiene tu id y llave RSA.

Ejemplo

```python
options = {}
options["rsa_public_key"] = self.rsa_public_key #"la llave pública RSA"
options["rsa_id"] = self.rsa_id # "el id de tu llave"
token = self.token.create(data=self.token_data, **options)

```

## Servicios

### Crear Token

Antes de crear un Cargo o Card es necesario crear un `token` de tarjeta. 
Lo recomendable es generar los 'tokens' con [Culqi Checkout v4](https://docs.culqi.com/es/documentacion/checkout/v4/culqi-checkout/) o [Culqi JS v4](https://docs.culqi.com/es/documentacion/culqi-js/v4/culqi-js/) **debido a que es muy importante que los datos de tarjeta sean enviados desde el dispositivo de tus clientes directamente a los servidores de Culqi**, para no poner en riesgo los datos sensibles de la tarjeta de crédito/débito.

> Recuerda que cuando interactúas directamente con el [API Token](https://apidocs.culqi.com/#tag/Tokens/operation/crear-token) necesitas cumplir la normativa de PCI DSS 3.2. Por ello, te pedimos que llenes el [formulario SAQ-D](https://listings.pcisecuritystandards.org/documents/SAQ_D_v3_Merchant.pdf) y lo envíes al buzón de riesgos Culqi.

```python

token = self.token.create(data=self.token_data)

```

### Crear Cargo

Crear un cargo significa cobrar una venta a una tarjeta. Para esto previamente deberías generar el  `token` y enviarlo en parámetro **source_id**.

Los cargos pueden ser creados vía [API de devolución](https://apidocs.culqi.com/#tag/Cargos/operation/crear-cargo).

```python
charge = self.charge.create(data=self.charge_data)
```

### Crear Devolución

Solicita la devolución de las compras de tus clientes (parcial o total) de forma gratuita a través del API y CulqiPanel. 

Las devoluciones pueden ser creados vía [API de devolución](https://apidocs.culqi.com/#tag/Devoluciones/operation/crear-devolucion).

```python
refund = self.refund.create(data=self.refund_data)
```

### Crear Customer

El **cliente** es un servicio que te permite guardar la información de tus clientes. Es un paso necesario para generar una [tarjeta](/es/documentacion/pagos-online/recurrencia/one-click/tarjetas).

Los clientes pueden ser creados vía [API de cliente](https://apidocs.culqi.com/#tag/Clientes/operation/crear-cliente).

```python
customer = self.customer.create(data=self.customer_data)
```

### Actualizar Customer

```python
updated_customer = self.customer.update(
        id_=created_customer["data"]["id"], data=metadatada
    )
```

### Obtener Customer

```python
 retrieved_customer = self.customer.read(created_customer["data"]["id"])
```

### Crear Card

La **tarjeta** es un servicio que te permite guardar la información de las tarjetas de crédito o débito de tus clientes para luego realizarles cargos one click o recurrentes (cargos posteriores sin que tus clientes vuelvan a ingresar los datos de su tarjeta).

Las tarjetas pueden ser creadas vía [API de tarjeta](https://apidocs.culqi.com/#tag/Tarjetas/operation/crear-tarjeta).

```python
 card = self.card.create(data=self.card_data)
```

### Crear Plan

El plan es un servicio que te permite definir con qué frecuencia deseas realizar cobros a tus clientes.

Un plan define el comportamiento de las suscripciones. Los planes pueden ser creados vía el [API de Plan](https://apidocs.culqi.com/#/planes#create) o desde el **CulqiPanel**.

```python
plan = self.plan.create(data=self.plan_data)
```

### Crear Suscripción

La suscripción es un servicio que asocia la tarjeta de un cliente con un plan establecido por el comercio.

Las suscripciones pueden ser creadas vía [API de suscripción](https://apidocs.culqi.com/#tag/Suscripciones/operation/crear-suscripcion).

```python
subscription = self.subscription.create(data=self.subscription_data)
```

### Crear Orden

Es un servicio que te permite generar una orden de pago para una compra potencial.
La orden contiene la información necesaria para la venta y es usado por el sistema de **PagoEfectivo** para realizar los pagos diferidos.

Las órdenes pueden ser creadas vía [API de orden](https://apidocs.culqi.com/#tag/Ordenes/operation/crear-orden).

```python
orden = self.orden.create(data=self.orden_data)
```

## Pruebas

En la caperta **/test** econtraras ejemplo para crear un token, charge, plan, órdenes, card, suscripciones, etc.

> Recuerda que si quieres probar tu integración, puedes utilizar nuestras [tarjetas de prueba.](https://docs.culqi.com/es/documentacion/pagos-online/tarjetas-de-prueba/)

### Ejemplo Prueba Token

```python
 @pytest.mark.vcr()
    def test_token_create(self):
        token = self.token.create(data=self.token_data)
        print(token)
        assert token["data"]["object"] == "token"

```

### Ejemplo Prueba Cargo
```python
 @property
    def charge_data(self):
        # pylint: disable=no-member
        token_data = deepcopy(Data.TOKEN)
        token = self.culqi.token.create(data=token_data)
        print(token)
        charge_data = deepcopy(Data.CHARGE)
        charge_data["source_id"] = token["data"]["id"]

        return charge_data

 @pytest.mark.vcr()
    def test_charge_create(self):
        charge = self.charge.create(data=self.charge_data)
        print (charge)
        assert charge["data"]["object"] == "charge"
```

## Documentación

- [Referencia de Documentación](https://docs.culqi.com/)
- [Referencia de API](https://apidocs.culqi.com/)
- [Demo Checkout V4 + Culqi 3DS](https://github.com/culqi/culqi-python-demo-checkoutv4-culqi3ds)
- [Wiki](https://github.com/culqi/culqi-python/wiki)

## Changelog

Todos los cambios en las versiones de esta biblioteca están listados en
[CHANGELOG.md](CHANGELOG.md).

## Autor
Team Culqi

## Licencia
El código fuente de culqi-python está distribuido bajo MIT License, revisar el archivo LICENSE.


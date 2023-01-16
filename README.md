# Culqi Python

[![Build Status](https://travis-ci.org/culqi/culqi-python.svg?branch=master)](https://travis-ci.org/culqi/culqi-python)
![](https://img.shields.io/pypi/pyversions/Culqi)
![](https://img.shields.io/pypi/l/culqi)
![](https://img.shields.io/pypi/v/culqi)


Nuestra Biblioteca PYTHON oficial de CULQI, es compatible con la v2.0 del Culqi API, con el cual tendrás la posibilidad de realizar cobros con tarjetas de débito y crédito, Yape, PagoEfectivo, billeteras móviles y Cuotéalo con solo unos simples pasos de configuración.

## Requisitos

- Python 2.7+
* Afiliate [aquí](https://afiliate.culqi.com/).
* Si vas a realizar pruebas obtén tus llaves desde [aquí](https://integ-panel.culqi.com/#/registro), si vas a realizar transacciones reales obtén tus llaves desde [aquí](https://panel.culqi.com/#/registro) (1).

> Recuerda que para obtener tus llaves debes ingresar a tu CulqiPanel > Desarrollo > ***API Keys***.

![alt tag](http://i.imgur.com/NhE6mS9.png)

> Recuerda que las credenciales son enviadas al correo que registraste en el proceso de afiliación.

## Instalación

Ejecuta los siguientes comandos:

```bash
py -m pip install pytest
py -m pip install python-dotenv
py -m pip install culqi
py -m pip install jsonschema

```

![](/resources/carbon.png)


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

- [Referencia de API](https://www.culqi.com/api/)
- [Demo Checkout V4 + Culqi 3DS](https://github.com/culqi/culqi-python-demo-checkoutv4-culqi3ds)
- [Wiki](https://github.com/culqi/culqi-python/wiki)

## Pruebas

En la caperta **/test** econtraras ejemplo para crear un token, charge,plan, órdenes, card, suscupciones, etc.

> Recuerda que si quieres probar tu integración, puedes utilizar nuestras [tarjetas de prueba.](https://docs.culqi.com/es/documentacion/pagos-online/tarjetas-de-prueba/)

## Changelog

Todos los cambios en las versiones de esta biblioteca están listados en
[CHANGELOG.md](CHANGELOG.md).

## Desarrollo
[Revisa nuestra guia de contribución](CONTRIBUTING.md)

## Contribuidores

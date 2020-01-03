<img src="resources/logo.png" style="float: right;" />

# Culqi Python

[![Build Status](https://travis-ci.org/culqi/culqi-python.svg?branch=master)](https://travis-ci.org/culqi/culqi-python)
![](https://img.shields.io/pypi/pyversions/Culqi)
![](https://img.shields.io/pypi/l/culqi)
![](https://img.shields.io/pypi/v/culqi)

<br/><br/>

Biblioteca de CULQI para el lenguaje Python, pagos simples en tu sitio web. 

## Requisitos

- Python 2.7, 3.5, 3.6, 3.7, 3.8-dev
- Credenciales de comercio en [Culqi](https://culqi.com).

## Instalación

```bash
pip install culqi 
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
- [Ejemplos](https://github.com/culqi/culqi-python/wiki)
- [Wiki](https://github.com/culqi/culqi-python/wiki)



## Changelog

Todos los cambios en las versiones de esta biblioteca están listados en
[CHANGELOG.md](CHANGELOG.md).

## Desarrollo
[Revisa nuestra guia de contribución](CONTRIBUTING.md)

## Contribuidores

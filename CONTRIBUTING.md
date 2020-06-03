# Cómo contribuir a este proyecto

> Si estas interesado en contribuir con el desarrollo y mantenimiento de este paquete
> es recomendable que emplees [poetry](https://poetry.eustace.io) para la gestión de
> dependencias y [pyenv](https://github.com/pyenv/pyenv) para la gestión de versiones
> de python.

## Entorno

Clona el proyecto

```bash
$ git clone https://github.com/culqi/culqi-python.git
$ cd culqi
```

Instala las dependencias

```bash
$ poetry install
```

## Testing and coverage

Puedes ejecutar los tests con poetry

```bash
poetry run pytest --cov --cov-report=
poetry run coverage report
```

En caso quieras ejecutar las pruebas en todas las versiones puedes emplear tox

## ¿Quieres enviar un PR?

Antes de hacer tu primer commit y enviar tu pull request ejecuta

```bash
$ poetry run pre-commit install
```

Luego realiza tu commits de forma habitual.

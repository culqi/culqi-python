# -*- encoding: utf-8 -*-
class ErrorCode:
    """Codigos de Denegación de Bancos.

    - EXPIRED_CARD
      Tarjeta vencida. La tarjeta está vencida o la fecha de vencimiento
      ingresada es incorrecta.

    - STOLEN_CARD
      Tarjeta robada. La tarjeta fue bloqueada y reportada al banco emisor
      como una tarjeta robada.

    - LOST_CARD
      Tarjeta perdida. La tarjeta fue bloqueada y reportada al banco emisor
      como una tarjeta perdida.

    - INSUFFICIENT_FUNDS
      Fondos insuficientes. La tarjeta no tiene fondos suficientes para
      realizar la compra.

    - CONTACT_ISSUER
      Contactar emisor. La operación fue denegada por el banco emisor de la
      tarjeta y el cliente necesita contactarse con la entidad para conocer
      el motivo.

    - INVALID_CVV
      CVV inválido. El código de seguridad (CVV2, CVC2, CID) de la tarjeta es
      inválido.

    - INCORRECT_CVV
      CVV incorrecto. El código de seguridad (CVV2, CVC2, CID) de la tarjeta
      es incorrecto.

    - TOO_MANY_ATTEMPTS_CVV
      Exceso CVV. El cliente ha intentado demasiadas veces ingresar el código
      de seguridad (CVV2, CVC2, CID) de la tarjeta.

    - ISSUER_NOT_AVAILABLE
      Emisor no disponible. El banco que emitió la tarjeta no responde. El
      cliente debe realizar el pago nuevamente.

    - ISSUER_DECLINE_OPERATION
      Operación denegada. La operación fue denegada por el banco emisor de la
      tarjeta por una razón desconocida.

    - INVALID_CARD
      Tarjeta inválida. La tarjeta utilizada tiene restricciones para este tipo
      de compras. El cliente necesita contactarse con el banco emisor para
      conocer el motivo de la denegación.

    - PROCESSING_ERROR
      Error de procesamiento. Ocurrió un error mientras procesabamos la compra.
      Contáctate con culqi.com/soporte para que te demos una solución.

    - FRAUDULENT
      Operación fraudulenta. El banco emisor de la tarjeta sospecha que se
      trata de una compra fraudulenta.

    - CULQI_CARD
      Tarjeta Culqi. Estás utilizando una tarjeta de pruebas de Culqi para
      realizar una compra real.
    """

    EXPIRED_CARD = "expired_card"
    STOLEN_CARD = "stolen_card"
    LOST_CARD = "lost_card"
    INSUFFICIENT_FUNDS = "insufficient_funds"
    CONTACT_ISSUER = "contact_issuer"
    INVALID_CVV = "invalid_cvv"
    INCORRECT_CVV = "incorrect_cvv"
    TOO_MANY_ATTEMPTS_CVV = "too_many_attempts_cvv"
    ISSUER_NOT_AVAILABLE = "issuer_not_available"
    ISSUER_DECLINE_OPERATION = "issuer_decline_operation"
    INVALID_CARD = "invalid_card"
    PROCESSING_ERROR = "processing_error"
    FRAUDULENT = "fraudulent"
    CULQI_CARD = "culqi_card"


class HTTPErrorCode:
    """Tipos de Errores.

    - INVALID_REQUEST_ERROR:
      HTTP 400 - La petición tiene una sintaxis inválida.

    - AUTHENTICATION_ERROR:
      HTTP 401 - La petición no pudo ser procesada debido a problemas con las
      llaves.

    - PARAMETER_ERROR:
      HTTP 422 - Algún parámetro de cualquier petición es inválido.

    - CARD_ERROR:
      HTTP 402 - No se pudo realizar el cargo a una tarjeta.

    - LIMIT_API_ERROR:
      HTTP 429 - Estás haciendo muchas peticiones rápidamente al API o
      superaste tu límite designado.

    - RESOURCE_ERROR:
      HTTP 404 - El recurso no puede ser encontrado, es inválido o tiene un
      estado diferente al permitido.

    - API_ERROR:
      HTTP 500 y 503 - Engloba cualquier otro tipo de error (Ejemplo: problema
      temporal con los servidores de Culqi) y debería de ocurrir muy pocas
      veces.
    """

    # HTTP 400
    INVALID_REQUEST_ERROR = "invalid_request_error"
    # HTTP 401
    AUTHENTICATION_ERROR = "authentication_error"
    # HTTP 422
    PARAMETER_ERROR = "parameter_error"
    # HTTP 402
    CARD_ERROR = "card_error"
    # HTTP 429
    LIMIT_API_ERROR = "limit_api_error"
    # HTTP 404
    RESOURCE_ERROR = "resource_error"
    # HTTP 500 503
    API_ERROR = "api_error"


class ErrorMessage:
    NOT_ALLOWED = "You can't perform this action."


class BadRequestError(Exception):
    pass


class GatewayError(Exception):
    pass


class ServerError(Exception):
    pass


class NotAllowedError(Exception):
    pass

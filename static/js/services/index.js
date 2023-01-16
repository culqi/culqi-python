class Service {
  #BASE_URL = "http://localhost:5100";

  #http = async ({ endPoint, method = 'POST', body = {}, headers = {} }) => {
    const authentication_3DS = body.authentication_3DS ? {
      eci: body.authentication_3DS.eci,
      xid: body.authentication_3DS.xid,
      cavv: body.authentication_3DS.cavv,
      protocolVersion: body.authentication_3DS.protocolVersion,
      directoryServerTransactionId: body.authentication_3DS.directoryServerTransactionId,
    } : null;
    try {
      const response = await fetch(`${this.#BASE_URL}/${endPoint}`,
        {
          headers: { 'Content-Type': 'application/json', ...headers },
          body: JSON.stringify(body),
          method
        });
      const responseJSON = await response;
      return { statusCode: response.status, data: responseJSON }
    } catch (err) {
      return { statusCode: 502, data: null }
    }
  }

  createCard = async (bodyCard) => {
    console.log("Entro createCard");
    console.log(JSON.stringify(bodyCard));
    return this.#http({ endPoint: "culqi/generateCards", body:bodyCard});
  }
  createCharge = async (bodyCharge) => {
    console.log("Entro createCard");
    console.log(JSON.stringify(bodyCharge));
    return this.#http({ endPoint: "culqi/generateCharge", body:bodyCharge});
  }
}
export default Service;

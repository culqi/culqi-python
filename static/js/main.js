import config from "./config/index.js";
import culqiConfig from "./config/checkout.js";
import "./config/culqi3ds.js";
import { generateCardImpl } from "./services/impl/index.js";

culqiConfig();

const deviceId = await Culqi3DS.generateDevice();

if (!deviceId) {
  console.log("Ocurrio un error al generar el deviceID");
}
let tokenId, email, customerId;

window.addEventListener("message", async function (event) {
  if (event.origin === window.location.origin) {
    const { parameters3DS, error } = event.data;

    if (parameters3DS) {
      let statusCode = null;
      const responseCard = await generateCardImpl({ customerId, deviceId, email, tokenId, parameters3DS });
      statusCode = responseCard.statusCode;

      if (statusCode === 200) {
        resultdivCard("TARJETA CREADA CON ÉXITO");
        Culqi3DS.reset();

      } else {
        resultdivCard("CREACIÓN DE TARJETA FALLIDA");
        Culqi3DS.reset();
      }
    }

    if (error) {
      resultdiv("Error, revisa la consola");
      console.log("Ocurrió un error: ", error);
    }
  }
},
  false
);

window.culqi = async () => {
  if (Culqi.token) {
    Culqi.close();
    tokenId = Culqi.token.id;
    email = Culqi.token.email;
    customerId = $("#idCustomer").val();

    const { statusCode } = await generateCardImpl({ customerId, deviceId, email, tokenId });
    validationInit3DS({ email, statusCode, tokenId });

  } else {
    alert(Culqi.error.user_message);
    $('#response-panel').show();
    $('#response').html(Culqi.error.merchant_message);
    $('body').waitMe('hide');
  }
};

const validationInit3DS = ({ statusCode, email, tokenId }) => {
  console.log(statusCode);
  console.log("statusCode");
  if (statusCode === 200) {

    Culqi3DS.settings = {
      charge: {
        totalAmount: config.TOTAL_AMOUNT,
        returnUrl: "http://localhost:5100/card"
      },
      card: {
        email: email,
      }
    };
    Culqi3DS.initAuthentication(tokenId);

  } else if (statusCode === 201) {
    resultdiv("PAGO EXITOSO - SIN 3DS");
    console
    Culqi3DS.reset();
  } else {
    resultdiv("PAGO FALLIDO");
    Culqi3DS.reset();

  }
}


$("#response-panel").hide();

function resultdivCard(message) {
  $('#response-panel').show();
  $('#response_card').html(message);
  // $('body').waitMe('hide');
}

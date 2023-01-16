import Service from "../index.js"
import config from "../../config/index.js"

const service = new Service();

export const generateCardImpl = async ({ customerId, email, tokenId, deviceId, parameters3DS = null }) => {
  var data_fraud = {
      device_finger_print_id: deviceId
  }

  var data = {
    amount : config.TOTAL_AMOUNT,
    currency_code : config.CURRENCY,
    email : email,
    token_id : tokenId,
    customer_id : customerId,
    antifraud_details : data_fraud
    };
    console.log("json jdd");
    console.log(data);

  return service.createCard(parameters3DS ? { ...data, authentication_3DS: { ...parameters3DS } } : data);
}

export const generateChargeImpl = async ({tokenId,  email, parameters3DS = null}) => {
  var data_fraud = {
   phone_number: "961778965"
}
  var data = {
    amount : config.TOTAL_AMOUNT,
    currency_code : config.CURRENCY,
    email : email,
    source_id : tokenId,
    antifraud_details : data_fraud
    };
    console.log("json");
    console.log(data);

  return service.createCharge(parameters3DS ? { ...data, authentication_3DS: { ...parameters3DS } } : data);
}

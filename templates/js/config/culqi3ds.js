import config from "./index.js"

Culqi3DS.options = {
    showModal: true,
    showLoading: true,
    showIcon: true,
    closeModalAction: () => window.location.reload(true),
    // style: {
    //     btnColor: "red",
    //     btnTextColor: "yellow",
    // },
};

Culqi3DS.publicKey = config.PUBLIC_KEY;
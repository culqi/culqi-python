$("#response-panel").hide();
$('#crearCustomer').on('click', function (e) {
  var address = $("#address").val();
  var address_city = $('#address_c').val()
  var country_code = $('#country').val()
  var email = $('#email').val()
  var first_name = $('#f_name').val()
  var last_name = $('#l_name').val()
  var phone_number = $('#phone').val()

  var data = {
    email : $("#email").val(),
    first_name : $('#f_name').val(),
    last_name : $('#l_name').val(),
    address : $('#address').val(),
    address_city : $('#address_c').val(),
    country_code : $('#country').val(),
    phone_number : $('#phone').val()};
  console.log(data);
  $.ajax({
    type: 'POST',
    url: 'http://localhost:5100/culqi/generateCustomer',
    data: JSON.stringify(data),
    contentType: "application/json",
    datatype: 'json',
    success: function (data) {
      console.log(data);
      var result = "";
      if (data.constructor == String) {
        result = JSON.parse(data);
      }
      if (data.constructor == Object) {
        result = JSON.parse(JSON.stringify(data));
      }
      if (result.object === 'customer') {
        resultdiv('Se creo el objeto Customer con el siguiente ID: ' + result.id);
      }
      if (result.object === 'error') {
        resultdiv(result);
        alert(result.merchant_message);
      }
    },
    error: function (error) {
      resultdiv(error)
    }
  });
  function resultdiv(message) {
    $('#response-panel').show();
    $('#response').html(message);
  }
});

const generateOrder = async () => {
  const response = await $.ajax({
    type: 'GET',
    url: 'http://localhost:8000/culqi-efectivo-examplev4-yape__3ds/ajax/order.php',
  });
  const responseJSON = await JSON.parse(response);
  if (responseJSON.object === "order") {
    return { status: 200, data: responseJSON }
  } else {
    return { status: 401, data: responseJSON }
  }
}

export default generateOrder;

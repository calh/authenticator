function ackHandler(e) {
  console.log("Successfully delivered the message with tID " + e.data.transactionId);
  console.log("data: " + JSON.stringify(e.data));
}

function nackHandler(e) {
  console.log("Unable to deliver message " + e.data.transactionId + ":  " + e.error.message);
}

function sendTimezoneToWatch() {
  // Retrieve the timezone as an hourly offset from UTC.
  // retains compatibility with the tZone format used in authenticator.c
  // and configuration.txt
  var tZone = new Date().getTimezoneOffset() / 60 * -1;
  // Send it to the watch
  console.log("Sending tZone: " + tZone);
  Pebble.sendAppMessage({ "tZone": tZone }, ackHandler, nackHandler)
}

function appMessageListener(e) {
  console.log("Got message!");
  console.log(e.payload.messageType);
  //switch(e.payload.messageType) {
  //}
}
Pebble.addEventListener("ready",
    function(e) {
      console.log("JavaScript app ready and running!");
      Pebble.addEventListener("appmessage", appMessageListener);
      sendTimezoneToWatch();
    }
);


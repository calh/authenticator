function sendTimezoneToWatch() {
  // Get the number of seconds to add to convert localtime to utc
  var tZone = new Date().getTimezoneOffset() / 60 * -1;
  // Send it to the watch
  console.log("Sending tZone: " + tZone);
  Pebble.sendAppMessage({ 'tZone': tZone })
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


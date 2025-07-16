#include <WiFi.h>
#include <WiFiUdp.h>
const char* ssid = "ESP32_AP";
const char* password = "12345678";
unsigned int localPort = 80;  // Local port to listen on
WiFiUDP Udp;

void setup() {
  Serial.begin(115200);
  delay(1000);
  WiFi.softAP(ssid, password);
  Udp.begin(localPort);
}

void loop() {
  
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    int byteReceived = Udp.read();
    if (byteReceived != -1) {
      Serial.print("Received byte: ");
      Serial.println(byteReceived, HEX);
    }
  }
}

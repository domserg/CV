
#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>
int robot_speed     = 12; //Controls speed (PWM) 
int robot_direction = 14; //Controls direction
int servo_left = 16;
int servo_right = 18;

// Set these to your desired credentials.
const char *ssid = "yourAP";
const char *password = "yourPassword";

WiFiServer server(80);

void setup() {
  pinMode(robot_speed, OUTPUT);
  pinMode(robot_direction, OUTPUT);
  pinMode(servo_left, OUTPUT);
  pinMode(servo_right, OUTPUT);

  Serial.begin(115200);
  Serial.println();
  Serial.println("Configuring access point...");
  // You can remove the password parameter if you want the AP to be open.
  // a valid password must have more than 7 characters
  while(!WiFi.softAP(ssid, password)) {
    Serial.println("Soft AP creation failed.");
  }
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  server.begin();
  Serial.println("Server started");
}

void loop() {
  WiFiClient client = server.available();   // listen for incoming clients
  if (client) {                             // if you get a client,
    Serial.println("New Client.");          // print a message out the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    while (client.connected()) {            // loop while the client's connected=
      if (client.available()) {
        char a = client.read();
        int d = int(a);
        //your code
        Serial.println(d);
        }
      }
    }
    // close the connection:
    client.stop();
    Serial.println("Client Disconnected.");
  }
}

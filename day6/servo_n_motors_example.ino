#include <ESP32Servo.h>

// create two servo objects
Servo servoLeft;
Servo servoRight;

// These are all GPIO pins on the ESP32
// Recommended pins include 2,4,12-19,21-23,25-27,32-33
int servoLeftPin = 26;
int servoRightPin = 27;


int pos = 90;      // position in degrees
//ESP32PWM pwm;

int motorPin1 = 13, motorPin2 = 14;

void setup() {
  // Allow allocation of all timers
  //ESP32PWM::allocateTimer(0);
  //ESP32PWM::allocateTimer(1);
  Serial.begin(115200);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  //servoLeft.setPeriodHertz(50);      // Standard 50hz servo
  //servoRight.setPeriodHertz(50);      // Standard 50hz servo
  servoLeft.attach(servoLeftPin);
  servoRight.attach(servoRightPin);
  servoLeft.write(90);
  servoRight.write(90);

}

void loop() {
  servoLeft.write(90);
  servoRight.write(90);
  delay(5000);
  servoLeft.write(2);
  servoRight.write(178);
  delay(500);
  servoLeft.write(90);
  servoRight.write(90);
  delay(5000);
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  delay(500);
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  delay(1000);
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  delay(500);
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  delay(1000);

  delay(5000);

}

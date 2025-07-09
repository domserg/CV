void setup() {
  pinMode(32, OUTPUT); //IN1
  pinMode(33, OUTPUT); //IN2
}
void loop() {
  analogWrite(32, 230); //High speed cw
  digitalWrite(33, LOW);
  delay(2000);
  analogWrite(32, 40); //Low speed cw
  digitalWrite(33, LOW);
  delay(2000);
  analogWrite(32, 10); //High speed ccw
  digitalWrite(33, HIGH);
  delay(2000);
  analogWrite(32, 215); //Low speed ccw
  digitalWrite(33, HIGH);
  delay(2000);
}

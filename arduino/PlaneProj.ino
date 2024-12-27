#include <Servo.h>
Servo servo;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  servo.attach(3);
  servo.write(0);
}

void loop() {
  while (!Serial.available());
  int x = Serial.readString().toInt();

  servo.write(x);
  delay(100);
}

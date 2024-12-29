#include <Servo.h>

Servo servos[2];
const byte servoPins[2] = {3, 4};
int runs = 0;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);

  for(int i = 0; i < 2; i++){
    servos[i].attach(servoPins[i]);
    servos[i].write(0);
  }
  
}

void loop() {
  while (!Serial.available());
  int x = Serial.readString().toInt();
  // did not feel like dealing with strings so keep a run amount
  runs % 2 == 0 ? servos[0].write(x) : servos[1].write(x);
  delay(100);
  runs++;
}
#include <Servo.h>

Servo servos[4];
const byte servoPins[4] = {3, 4, 5, 6};
int runs = 0;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);

  for(int i = 0; i < 4; i++){
    servos[i].attach(servoPins[i]);
    servos[i].write(0);
  }
  
}

void loop() {
  while (!Serial.available());
  int x = Serial.readString().toInt();
  // did not feel like dealing with strings so keep a run amount
  if (runs % 2 == 0) {
    servos[0].write(x);
    servos[1].write(x);
  } else {
    servos[2].write(x);
    servos[3].write(x);
  }
  delay(100);
  runs++;
}
#include <Stepper.h>

#define STEPS 64

Stepper stepper(STEPS, 1, 2, 3, 4);

int elozo = 0;

void setup() {
  
  stepper.setSpeed(100);

}

void loop() {
  
  int val = analogRead(0);

  stepper.step(val - elozo);

  elozo = val;

}

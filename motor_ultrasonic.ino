#include <HCSR04.h>
#include <CheapStepper.h>


CheapStepper stepper (8,9,10,11);
boolean moveClockwise = true;


UltraSonicDistanceSensor distanceSensor(6, 7);  // Initialize sensor that uses digital pins 13 and 12.

void setup () {

    stepper.setRpm(20);

    Serial.begin(9600);  // We initialize serial connection so that we could print values from sensor.
}

void loop () {
    moveClockwise = true;
    stepper.moveToDegree(moveClockwise, 0);
    delay(100);

    moveClockwise = false;

    for (int i=0; i<360; i+=2) {
      stepper.moveDegrees(moveClockwise, 2);
      Serial.print(i);
      Serial.print('-');
      Serial.println(distanceSensor.measureDistanceCm());

      Serial.println();
      delay(100);
    }
}

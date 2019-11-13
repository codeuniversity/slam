/*
 * cheapStepper_move.ino
 * ///////////////////////////////////////////
 * using CheapStepper Arduino library v.0.2.0
 * created by Tyler Henry, 7/2016
 * ///////////////////////////////////////////
 * 
 * This sketch illustrates the library's
 * "blocking" move functions -
 * i.e. the move will "pause" the arduino sketch
 * -- for non-blocking moves, see cheapStepper_newMoveTo.ino example
 * 
 * This sketch also shows how to set the RPM
 * and shows a few different types of move functions
 * - by steps or by degrees.
 * 
 * Blocking moves are useful if you need a specific RPM
 * but don't need your arduino to perform other functions
 * while the stepper is moving.
 * 
 * //////////////////////////////////////////////////////
 */

// first, include the library :)

#include <CheapStepper.h>
#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;

// next, declare the stepper
// and connect pins 8,9,10,11 to IN1,IN2,IN3,IN4 on ULN2003 board


CheapStepper stepper (8,9,10,11); 

// let's create a boolean variable to save the direction of our rotation

boolean moveClockwise = true;


void setup() {

  // let's set a custom speed of 20rpm (the default is ~16.25rpm)
  
  stepper.setRpm(20); 
  /* Note: CheapStepper library assumes you are powering your 28BYJ-48 stepper
   * using an external 5V power supply (>100mA) for RPM calculations
   * -- don't try to power the stepper directly from the Arduino
   * 
   * accepted RPM range: 6RPM (may overheat) - 24RPM (may skip)
   * ideal range: 10RPM (safe, high torque) - 22RPM (fast, low torque)
   */

  // now let's set up a serial connection and print some stepper info to the console
  
  Serial.begin(9600); 
  Wire.begin();
  
  sensor.init();
  sensor.setTimeout(500);
  sensor.startContinuous();       
  
}

void loop() {

    // let's do a clockwise move first
  
    moveClockwise = true;
    stepper.moveToDegree(moveClockwise, 0);
    delay(100);

    moveClockwise = false;

    for (int i=1; i<360; i+=1) {
      // The Arduino sketch "pauses" during move()
      stepper.moveDegrees(moveClockwise, 1);
      Serial.print(i);
      Serial.print('-');
      Serial.print(sensor.readRangeContinuousMillimeters());
      if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }

      Serial.println();
      delay(10);
    }
    
}

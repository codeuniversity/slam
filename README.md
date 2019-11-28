# SLAM

SLAM allows our robot to locate itself and map its environment simultaneously.
This programm extracts distinct features, also known as landmarks (e.g wall corners), from the range measurement (360 degrees) of the Lidar sensor.
It then tries to match these newly found landmarks with previous observed ones to estimate the robot's current position.
 


1. **Requirements**
2. **Usage**
3. **Project architecture**

## 1. Requirements

- python3
- [MHIST](https://github.com/alexmorten/mhist)

MHIST is a simple on disc measurement data base that stores and redistributes measurements consisting of a name, a value and optionally a timestamp through [grpc](https://github.com/grpc).

## 2. Usage 

Hardware used:
- micro controller: Arduino Uno
- single board computer: Raspberry Pi
- motor: 28BYJ-48 stepper motor (with ULN2003 driver board)
- rangefinder: Lidar sensor VL6180 VL6180X (30cm range)

The [low level controller](https://github.com/codeuniversity/slam/blob/master/motor_lidar/motor_lidar.ino) that runs on the Arduino continuously turns the motor by 360 degrees (it turns back to 0 degrees counterclockwise after each rotation). The sensor is fixed on the motor and measures the distance to objects in the environment. [Nervo](https://github.com/codeuniversity/nervo) receives the range measurements and rotation data and puts them into MHIST from which SLAM can then retrieve the data.

1. run [nervo](https://github.com/codeuniversity/nervo) and [MHIST](https://github.com/alexmorten/mhist)

2. run the [low level_controller](https://github.com/codeuniversity/slam/blob/master/motor_lidar/motor_lidar.ino)

3. run SLAM with `make run`


## 3. Project architecture

![alt](SLAM_diagram%20(3).png)

The receiver continuously receives range data from MHIST and creates point batches of data from one full turn. 

Then landmark extractor iterates through the point batch and compares the distance from the robot to adjacent points. If the difference of the ranges exceeds a defined threshold (depends on the range of the used sensor) a landmark of this area (described by 3 adjacent points) is created. 

Those extracted landmarks are then matched with already observed landmarks from previous measurements in landmark matcher. 

From matched landmarks we can estimate the new robot position. Knowing the position we can globalize the newly found landmarks and then add these to stored landmarks. We then also globalize the points. 

Lastly, we send both the position of the robot as well as the points to MHIST so that the [high-level-controller](https://github.com/codeuniversity/control-high) can retrieve the data and further plan the robot's trajectory.



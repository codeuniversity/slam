# SLAM

Our implementation of "SLAM"[^1] allows our robot to locate itself and map its environment simultaneously by measuring the environtment and performing landmark[^2] extracting and matching.

1. [Requirements](#1-requirements)
2. [Usage](#2-usage)
3. [Project architecture](#3-project-architecture)

### 1. Requirements

- python3
- [low level_controller](https://github.com/codeuniversity/slam/blob/master/motor_lidar/motor_lidar.ino) - continuously turns our motor (28BYJ-48 stepper) on which our Lidar sensor (VL6180 VL6180X) is fixated by 360 degrees. Range measurements of the environment on the horiuzontal level of the sensor are thereby taken.
- [nervo](https://github.com/codeuniversity/nervo) - receives the measurements and respective rotation data and puts them into MHIST.
- [MHIST](https://github.com/alexmorten/mhist) - is a simple on-disc measurement data base that stores and redistributes measurements consisting of a name, a value and optionally a timestamp through [grpc](https://github.com/grpc).

### 2. Usage 

1. run [nervo](https://github.com/codeuniversity/nervo) and [MHIST](https://github.com/alexmorten/mhist) on Raspberry Pi
2. run [low level_controller](https://github.com/codeuniversity/slam/blob/master/motor_lidar/motor_lidar.ino) on Arduino
3. run SLAM with `make run` on Raspberry Pi

### 3. Project architecture 
<br/><br/>
![alt](SLAM_diagram.png)

<br/><br/>
The "landmark extractor" iterates through the point batch (where the points are trigonometrically derived from the range and rotation data) and extracts local "spike landmarks"[^3]. Local means it is relative to the robot's current position instead of to the origin (i.e. the robot's first position).\
Those extracted landmarks are then "matched" (as in set in comparison and paired in the case of sufficient likeness) with landmarks from previous measurement rounds in the landmark matcher.\
From these matched landmarks the new robot position is estimated. With the position the new landmarks are globalized so that they are relative to the origin. They are then added to "stored landmarks". The point batch is also globalised.\
Lastly, both the position of the robot as well as the global points are sent to MHIST so that the [high-level-controller](https://github.com/codeuniversity/control-high) can retrieve the data and plan and optimise the robot's further trajectory.
<br/>

[^1]: "Simultaneous localization and mapping is the computational problem of constructing or updating a map of an unknown environment while simultaneously keeping track of an agent's location within it." - [wikipedia](https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping) 
[^2]: "A prominent identifying feature of a landscape." -[wordnik](https://www.wordnik.com/words/landmark)
[^3]: "The spike landmark extraction uses extrema to find landmarks. They are identified
by finding values in the range of a laser scan where two values differ by more than a
certain amount, e.g. 0.5 meters." - [SLAM for dummies](https://dspace.mit.edu/bitstream/handle/1721.1/119149/16-412j-spring-2005/contents/projects/1aslam_blas_repo.pdf)


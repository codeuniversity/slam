import serial
import numpy as np
import matplotlib.pyplot as plt
import math


# get serial port -> Arduino -> Tools -> Port
SERIAL_PORT = '/dev/cu.usbmodem1421'
SERIAL_RATE = 9600

def scatterPlots(results):
        x_values = []
        y_values = []
        for i in range(len(results)):
                x = (results[i][1] * math.cos(math.radians(results[i][0]))) # x = distance * cos(angle)
                y = (results[i][1] * math.sin(math.radians(results[i][0]))) # y = distance * sin(angle)
                x_values.append(x)
                y_values.append(y)
        plt.scatter(x_values, y_values)
        plt.title('Lidar Map')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


def main():
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    results = []
    while True:
        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println() on the Arduino
        reading = ser.readline().decode('utf-8')
        reading = reading[:-1]
        try:
                degree, distance = reading.split("-")
                degree = int(degree)
                distance = int(distance)

        except ValueError:
                continue

        results.append([degree, distance])
        print(degree, distance)

        # after one full 360° measurement start with the x/y calculation and mapping
        if degree == 358:
                scatterPlots(results)


if __name__ == "__main__":
    main()

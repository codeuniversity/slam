import serial
import numpy as np
import matplotlib.pyplot as plt
import math


# get serial port -> Arduino -> Tools -> Port
SERIAL_PORT = '/dev/cu.usbmodem14101'
SERIAL_RATE = 9600


#laserdata [[degree,distance],...]
#coordinates [[x_value,y_value],...]


def extract_spike_landmark(laserdata, coordinates):
    #array that stores found landmarks:
    new_landmarks_data = []

    threshold = 300 #in mm
    for i in range(len(laserdata)-2): #i = degree

        #check if distance threshold between two ranges is exceeded
        if (abs(laserdata[i][1]-laserdata[i+1][1])) >= threshold:
            vector1 = [coordinates[i][0]-coordinates[i+1][0]*(-1), coordinates[i][1]-coordinates[i+1][1]*(-1)]
            vector2 = [coordinates[i+1][0]-coordinates[i+2][0]*(-1), coordinates[i+1][1]-coordinates[i+2][1]*(-1)]
            landmark = {}
            landmark['pointA'] = coordinates[i]
            landmark['pointB'] = coordinates[i+1]
            landmark['pointC'] = coordinates[i+2]
            landmark['vector_AB'] = vector1
            landmark['vector_BC'] = vector2
            landmark['angle_A'] = laserdata[i][0]
            landmark['distance_A'] = laserdata[i][0]
            landmark['angle_B'] = laserdata[i+1][0]
            landmark['distance_B'] = laserdata[i+1][1]
            landmark['angle_C'] = laserdata[i+2][0]
            landmark['distance_C'] = laserdata[i+2][1]
            new_landmarks_data.append(landmark)

    for landmark in new_landmarks_data:
        print("Landmark found at points: pointA {} pointB {} pointC {}".format(landmark['pointA'], landmark['pointB'], landmark['pointC']))
        print("vector from pointA to pointB: {} vector from pointB to pointC: {} \n".format(landmark['vector_AB'],landmark['vector_BC']))

    return new_landmarks_data


#map landmarks to point cloud
def map_landmarks(new_landmarks_data, total_landmarks):
    #compare vectors
    for landmark in new_landmarks_data:
        for existing_landmark in total_landmarks:
            if landmark['vector_AB']==existing_landmark['vector_AB'] and landmark['vector_BC']==landmark['vector_BC']:
                estimate_robot_position(landmark)
            else:
                total_landmarks.append(landmark)
    return total_landmarks

def estimate_robot_position(landmark):
    vector_A = landmark['point_A']
    angle_A = landmark['angle_A']
    alpha_A = calculate_alpha(angle_A)
    distance_ZA = landmark['distance_A']
    ZAx = math.sin(alpha_A)*distance_ZA
    ZAy = math.cos(alpha_A)*distance_ZA

    robot_Z1 = [vector_A[0]+ZAx,vector_A[1]+ZAy]

    point_B = landmark['point_B']
    angle_B = landmark['angle_B']
    point_C = landmark['point_C']
    angle_C = landmark['angle_C']


def calculate_alpha(stepper_angle):
    if 0<stepper_angle<=90:
        return math.radians(90-stepper_angle)
    elif 90<stepper_angle<=180:
        return math.radians(180-stepper_angle)
    elif 180<stepper_angle<=270:
        return math.radians(270-stepper_angle)
    else:
        return math.radians(360-stepper_angle)




def scatterPlots(laserdata):
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
        coordinates = [zip(x_values, y_values)]
        return coordinates

def main():
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    laser_data = []
    total_landmarks = []
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

        laser_data.append([degree, distance])
        print(degree, distance)

        # after one full 360° measurement start with the x/y calculation and mapping
        if degree == 359:
                coordinates= scatterPlots(laser_data)

    new_landmarks_data = extract_spike_landmark(laser_data, coordinates)
    map_landmarks(new_landmarks_data, total_landmarks)


if __name__ == "__main__":
    main()

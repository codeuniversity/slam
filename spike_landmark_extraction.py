import numpy as np
import math
#laserdata [[degree,distance],...]
#coordinates [[x_value,y_value],...]

def extract_spike_landmark(laserdata, coordinates):
    #array that stores found landmarks:
    landmarks = []

    threshold = 300 #in mm
    for i in range(len(laserdata)-2): #i = degree
        #print(results[i][1]-results[i+1][1])
        #check if distance threshold between two ranges is exceeded
        if (laserdata[i][1]-laserdata[i+1][1])*(-1) >= threshold:
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
            landmarks.append(landmark)

    for landmark in landmarks:
        print("Landmark found at points: pointA {} pointB {} pointC {}".format(landmark['pointA'], landmark['pointB'], landmark['pointC']))
        print("vector from pointA to pointB: {} vector from pointB to pointC: {} \n".format(landmark['vector_AB'],landmark['vector_BC']))

    return landmarks


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

    robot_Z = [vector_A[0]+ZAx,vector_A[1]+ZAy]

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



if __name__=="__main__":
    #results = [[0, 30], [1, 340], [2, 100], [3, 400], [4, 200]]
    #laserdata = [(1, 5), (10, 34), (5, 50), (30, 10), (30, 10)]
    #total_landmarks = []
    #while new map from serial_lidar.py:
    #   new_landmarks_data = extract_spike_landmark(results,laserdata)
    #   map_landmarks(new_landmarks_data, total_landmarks)



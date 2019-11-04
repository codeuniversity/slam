existing_landmarks = []
import numpy as np


def extract_spike_landmark(results, laserdata):
    #array to keep track of found landmarks:
    landmarks = []
    # landmark [first point, second point, third point, vector from first to second point, vector from second to third point]
    threshold = 300 #in mm
    for i in range(len(results)-2): #i = degree
        #print(results[i][1]-results[i+1][1])
        #check if distance threshold between two ranges is exceeded
        if (results[i][1]-results[i+1][1])*(-1) >= threshold:
            vector1 = [laserdata[i][0]-laserdata[i+1][0]*(-1), laserdata[i][1]-laserdata[i+1][1]*(-1)]
            vector2 = [laserdata[i+1][0]-laserdata[i+2][0]*(-1), laserdata[i+1][1]-laserdata[i+2][1]*(-1)]
            landmarks.append([[laserdata[i], laserdata[i + 1], laserdata[i + 2]], vector1, vector2])

    for landmark in landmarks:
        print("Landmark found at points: point1 {} point2 {} point3 {}".format(landmark[0][0], landmark[0][1], landmark[0][2]))
        print("vector from point1 to point2: {} vector from point2 to point3: {} \n".format(landmark[1],landmark[2]))

    return landmarks


#map landmarks to point cloud
def map_landmarks(landmarks, existing_landmarks):
    #compare vectors
    for landmark in landmarks:
        for existing_landmark in existing_landmarks:
            if landmark[1]==existing_landmark[1] and landmark[2]==landmark[2]:
                estimate_robot_position(landmark, results)
            else:
                existing_landmarks.landmark

def estimate_robot_position(landmark, results, laserdata):
    point1 = landmark[0][0]
    point2 = landmark[0][1]
    distance_point_point2 =
    robot_position =
    distance from robot to point1
    distance from robot to point2








results = [[0, 30], [1,340],[2,100], [3,400], [4,200]]
laserdata = [(1,5), (10,34), (5,50), (30,10), (30,10)]
extract_spike_landmark(results,laserdata)



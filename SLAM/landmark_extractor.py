import SLAM.receiver
import SLAM.core

def extract_spike_landmark(points):
    #array that stores found landmarks:
    landmarks = []

    threshold = 200 #in mm
    for i in range(len(points)-2): #i = degree

        #check if distance threshold between two ranges is exceeded
        if (abs(points[i].distance-points[i+1].distance)) >= threshold:
            landmark = SLAM.core.Landmark(points[i],points[i+1],points[i+2])
            landmarks.append(landmark)

    for landmark in landmarks:
        print("Landmark found at points: A {} B {} C {}".format(landmark.A, landmark.B, landmark.C))
        print("vector AB: {} vector BC: {} \n".format(landmark.AB,landmark.BC))

    return landmarks


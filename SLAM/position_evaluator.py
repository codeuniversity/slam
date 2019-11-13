import SLAM.landmark_matcher.py
import math

def evaluate_position(landmark):
    alpha_A = calculate_alpha(landmark.A.rotation)
    ZAx = math.sin(alpha_A)*landmark.A.distance
    ZAy = math.cos(alpha_A)*landmark.A.distance
    robot_A = [landmark.A.x+ZAx,landmark.A.y+ZAy]

    alpha_B = calculate_alpha(landmark.B.rotation)
    ZBx = math.sin(alpha_B)*landmark.B.distance
    ZBy = math.cos(alpha_B)*landmark.B.distance
    robot_B = [landmark.B.x+ZBx,landmark.B.y+ZBy]

    alpha_C = calculate_alpha(landmark.C.rotation)
    ZCx = math.sin(alpha_C) * landmark.C.distance
    ZCy = math.cos(alpha_C) * landmark.C.distance
    robot_C = [landmark.B.x+ZCx,landmark.C.y+ZCy]



def calculate_alpha(stepper_angle):
    if 0<stepper_angle<=90:
        return math.radians(90-stepper_angle)
    elif 90<stepper_angle<=180:
        return math.radians(180-stepper_angle)
    elif 180<stepper_angle<=270:
        return math.radians(270-stepper_angle)
    else:
        return math.radians(360-stepper_angle)


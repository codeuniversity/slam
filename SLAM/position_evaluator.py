import SLAM.landmark_matcher
from SLAM.core import Point
import math


def evaluate_avg_position(landmarks):
    point_sum = Point(None, None, 0, 0)
    for l in landmarks:
        point_sum = point_sum + l.get_avg_robot_position()

    avg = sum/len(landmarks)
    return avg

import SLAM.core
from SLAM.landmark_extractor import extract_spike_landmarks
from SLAM.landmark_matcher import match_landmarks
from SLAM.position_evaluator import evaluate_position
from SLAM.receiver import Receiver
from multiprocessing import Queue
from SLAM.globalizer import *
from SLAM.sender import *

# creates point objects
def create_points(point_batch):
    points = []
    for p in point_batch:
        points.append(SLAM.core.Point(p[0], p[1]))
    return points


def main():
    stored_landmarks = []
    queue = Queue()
    receiver = Receiver(queue)
    receiver.start()
    for point_batch in queue.get():
        local_points = create_points(point_batch) #local points
        found_landmarks = extract_spike_landmarks(local_points)   #local landmarks
        matched_landmarks,new_landmarks = match_landmarks(found_landmarks, stored_landmarks)

        robot_position = evaluate_position(matched_landmarks)
        new_global_landmarks = globalize_landmarks(robot_position, new_landmarks)
        global_points = globalize_points(local_points)

        stored_landmarks.append(new_global_landmarks)
        send_points(global_points)
        send_position(robot_position)


    return stored_landmarks,global_points




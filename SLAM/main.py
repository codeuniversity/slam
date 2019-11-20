import SLAM.core
from SLAM.landmark_extractor import extract_spike_landmarks
from SLAM.landmark_matcher import match_landmarks
from SLAM.position_evaluator import evaluate_position
from SLAM.receiver import Receiver
from multiprocessing import Queue

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
    robot_trace = []
    global_points = []
    for point_batch in queue.get():
        points = create_points(point_batch)
        landmarks = extract_spike_landmarks(points)
        matched_landmarks = match_landmarks(landmarks)
        robot_position = evaluate_position(matched_landmarks[0])
        global_points.append(robot_trace.append(robot_position,points))






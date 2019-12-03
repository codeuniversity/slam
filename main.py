from SLAM.core import Point, Landmark
from SLAM.landmark_extractor import extract_spike_landmarks
from SLAM.landmark_matcher import match_landmarks
from SLAM.position_evaluator import evaluate_avg_position
from SLAM.receiver import Receiver
from multiprocessing import Queue
from SLAM.globalizer import globalize_points, globalize_landmarks
from SLAM.sender import send_points, send_position

# creates point objects
def create_points(point_batch):
    points = []
    for p in point_batch:
        points.append(Point(p[0], p[1]))
    return points


def main():
    first_iteration=True
    stored_landmarks = []
    queue = Queue()
    receiver = Receiver(queue)
    receiver.start()
    new_landmarks=[]
    point_cloud=[]
    while True:
        point_batch = queue.get()
        point_cloud = create_points(point_batch) #local points
        found_landmarks = extract_spike_landmarks(point_cloud)   #local landmarks
        matched_landmarks,new_landmarks = match_landmarks(found_landmarks, stored_landmarks)

        if first_iteration:
            robot_position = Point(None, None, x=0, y=0)
            first_iteration = False
        elif len(matched_landmarks) > 0:
            robot_position = evaluate_avg_position(matched_landmarks)
            new_landmarks = globalize_landmarks(robot_position, new_landmarks)
            point_cloud = globalize_points(robot_position, point_cloud)
        else:
            continue

        stored_landmarks.extend(new_landmarks)
        send_points(point_cloud)
        send_position(robot_position)

    return stored_landmarks, new_landmarks, point_cloud

if __name__ == '__main__':
    main()

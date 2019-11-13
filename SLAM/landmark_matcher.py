import SLAM.landmark_extractor
import SLAM.position_evaluator

total_landmarks = []

def match_landmarks(landmarks, stored_landmarks):
    #compare vectors
    for landmark in landmarks:
        for existing_landmark in stored_landmarks:
            if landmark.AB==existing_landmark.AB and landmark.BC==landmark.BC:
                SLAM.position_evaluator(landmark)
            else:
                total_landmarks.append(landmark)
    return total_landmarks
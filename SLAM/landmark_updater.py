from SLAM.core import Landmark

def update_matched_landmarks(matched_landmarks, stored_landmarks, robot_position):

    for landmark in matched_landmarks:
        re_globalize_landmark(landmark)
        for i in range(len(stored_landmarks)):
            if landmark == stored_landmarks[i]:
                stored_landmarks[i].A = (landmark.A + stored_landmarks[i].A)/2
                stored_landmarks[i].B = (landmark.B + stored_landmarks[i].B)/2
                stored_landmarks[i].C = (landmark.C + stored_landmarks[i].C)/2

def re_globalize_landmark(landmark:Landmark, robot_position):
    rp_vector_A = landmark.calculate_rp_vector(landmark.A)
    rp_vector_B = landmark.calculate_rp_vector(landmark.B)
    rp_vector_C = landmark.calculate_rp_vector(landmark.C)

    landmark.A = robot_position - rp_vector_A
    landmark.B = robot_position - rp_vector_B
    landmark.C = robot_position - rp_vector_C



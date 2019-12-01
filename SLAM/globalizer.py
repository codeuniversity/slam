
#translates local coordinates to global coordinates
def globalize_points(robot_position,local_coordinates):
    global_coordinates = []
    for local_coordinate in local_coordinates:
        local_coordinate = local_coordinate+robot_position
        global_coordinates.append(local_coordinate)
    return global_coordinates

def globalize_landmarks(robot_position,local_landmarks):
    global_landmarks = []
    for local_landmark in local_landmarks:
        local_landmark.A = local_landmark.A+robot_position
        local_landmark.B = local_landmark.B+robot_position
        local_landmark.C = local_landmark.C+robot_position
        global_landmarks.append(local_landmark)
    return global_landmarks




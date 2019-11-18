
#translates local coordinates to global coordinates
def point_cloud_generator(robot_position,local_coordinates):
    global_coordinates = []
    for local_coordinate in local_coordinates:
        local_coordinate = local_coordinate+robot_position
        global_coordinates.append(local_coordinate)

    return global_coordinates


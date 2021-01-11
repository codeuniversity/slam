import math

def calculate_alpha(stepper_angle):
    if 0 < stepper_angle <= 90:
        return math.radians(90-stepper_angle)
    elif 90 < stepper_angle <= 180:
        return math.radians(180-stepper_angle)
    elif 180 < stepper_angle <= 270:
        return math.radians(270-stepper_angle)
    else:
        return math.radians(360-stepper_angle)

class Point:
    def __init__(self,rotation,distance,x=None,y=None):
        self.rotation = rotation
        self.distance = distance

        if x is not None and y is not None:
            self.x=x
            self.y=y
        else:
            self.x = (distance * math.cos(math.radians(rotation)))
            self.y = (distance * math.sin(math.radians(rotation)))

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(None, None, x=new_x, y=new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y + other.y
        return Point(None, None, x = new_x, y = new_y)

    def __truediv__(self, other):
        new_x = self.x/other
        new_y = self.y/other
        return Point(None, None, x=new_x, y=new_y)

    def __str__(self):
        string = "x={} y={}".format(self.x,self.y)
        return string



class Landmark:
    def __init__(self,A:Point,B:Point,C:Point):
        self.A = A
        self.B = B
        self.C = C

        self.AB = [B.x - A.x, B.y - A.y]
        self.BC = [C.x - B.x, C.y - B.y]

    def __eq__(self, other_landmark):
        if self.AB==other_landmark.AB and self.BC == other_landmark.BC:
            return True
        else:
            return False

    def transfer_coordinates(self,other_landmark):
        self.A.x = other_landmark.A.x
        self.A.y = other_landmark.A.y
        self.B.x = other_landmark.B.x
        self.B.y = other_landmark.B.y
        self.C.x = other_landmark.C.x
        self.C.y = other_landmark.C.y


    def calculate_rp_vector(self, point):
        alpha = calculate_alpha(point.rotation)
        x = math.sin(alpha) * point.distance
        y = math.cos(alpha) * point.distance
        rp_vector = Point(None, None, x, y)
        return rp_vector


    def get_avg_robot_position(self):
        alpha_A = calculate_alpha(self.A.rotation)
        ZAx = math.sin(alpha_A)*self.A.distance
        ZAy = math.cos(alpha_A)*self.A.distance
        robot_A = Point(None, None, x=self.A.x+ZAx, y=self.A.y+ZAy)

        alpha_B = calculate_alpha(self.B.rotation)
        ZBx = math.sin(alpha_B)*self.B.distance
        ZBy = math.cos(alpha_B)*self.B.distance
        robot_B = Point(None, None, x=self.B.x+ZBx, y=self.B.y+ZBy)

        alpha_C = calculate_alpha(self.C.rotation)
        ZCx = math.sin(alpha_C) * self.C.distance
        ZCy = math.cos(alpha_C) * self.C.distance
        robot_C = Point(None, None, x=self.B.x+ZCx, y=self.C.y+ZCy)

        robot_position = (robot_A+robot_B+robot_C)/3
        return robot_position

import math

class Point:
    def __init__(self,rotation,distance):
        self.rotation = rotation
        self.distance = distance

        self.x = (distance * math.cos(math.radians(rotation)))
        self.y = (distance * math.sin(math.radians(rotation)))


class Landmark:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

        self.AB = [B.x - A.x, B.y - A.y]
        self.BC = [C.x - B.x, C.y - B.y]


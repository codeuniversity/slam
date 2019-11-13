import math

class Point:
    def __init__(self,rotation,distance):
        self.rotation = rotation
        self.distance = distance

        x = (distance * math.cos(math.radians(rotation)))
        y = (distance * math.sin(math.radians(rotation)))


class Landmark:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
        AB = [B.x - A.x, B.y - A.y]
        BC = [C.x - B.x, C.y - B.y]
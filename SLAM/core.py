import math

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

    def __truediv__(self, other):
        new_x = self.x/other
        new_y = self.y/other
        return Point(None, None, x=new_x, y=new_y)

    def __str__(self):
        string = "x={} y={}".format(self.x,self.y)
        return string



class Landmark:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

        self.AB = [B.x - A.x, B.y - A.y]
        self.BC = [C.x - B.x, C.y - B.y]


import math
class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def print_point(self):
        print('(%g, %g)'%self.x,self.y)
    
    def distace_between_points(self,other):
        distance = math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return distance

    def __str__(self):
        return '%g, %g'%(self.x, self.y)
    
    def __add__(self,other):
        n = self.x + other.x
        m = self.y + other.y
        new_point = Point(n,m)
        return new_point

point1 = Point(5,10)
point2 = Point(2,3)
print(point2)
print(point1.distace_between_points(point2))
print(point1+point2)


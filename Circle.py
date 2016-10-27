from point1 import *

class Circle:
    '''
represents a Circle.
attributes: center, radius.
    '''



def point_in_circle(c1,p1):
    '''
takes a Circle and a Point and 
returns True if the Point lies in 
or on the boundary of the circle
    '''
    distance = distance_between_points(c1.center,p1)
    if distance <= c1.radius:
        return True
    else:
        return False

def rect_in_circle(circle,rectangle):
    d1 = distance_between_points(circle.center,rectangle.corner)
    if d1 > circle.radius:
        return False
    rectangle.corner.x += rectangle.width   
    d2 = distance_between_points(circle.center,rectangle.corner)
    if d2 > circle.radius:
        return False
    rectangle.corner.y += rectange.height
    d3 = distance_between_points(cicle.center,rectangle.corner)
    if d3 > circle.radius:
        return False
    rectangle.corner.x -= rectangle.width
    d4 = distance_between_points(circle.center,rectange.corner)
    if d4 > circle.radius:
        return False
    return True

def rect_circle_overlap(circle,rectange):
    d1 = distance_between_points(circle.center,rectangle.corner)
    if d1 < circle.radius:
        return True
    rectangle.corner.x += rectangle.width   
    d2 = distance_between_points(circle.center,rectangle.corner)
    if d2 < circle.radius:
        return True
    rectangle.corner.y += rectange.height
    d3 = distance_between_points(cicle.center,rectangle.corner)
    if d3 < circle.radius:
        return True
    rectangle.corner.x -= rectangle.width
    d4 = distance_between_points(circle.center,rectange.corner)
    if d4 < circle.radius:
        return True
    return False



def main():
    my_circle = Circle()
    my_circle.radius = 75.0
    my_circle.center = Point()
    my_circle.center.x = 150.0
    my_circle.center.y = 100.0

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print(rect_in_circle(my_circle,box))

if __name__ == '__main__':
    main()

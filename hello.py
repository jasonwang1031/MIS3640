import turtle
import math
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

def oval(t):
        t.lt(50)
        arc(t,100,80)
        A.lt(100)
        arc(t,100,80)
        A.lt(50)

def graph(t):
    for i in range(6):
        oval(t)
        arc(A,130,60)


A=turtle.Turtle()
graph(A)


turtle.mainloop()
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


#graph 1
def inner(t):
    polygon(t,3,150)
    t.fd(75)
    circle(t,43.3)
    t.back(75)
    t.rt(30)

def graph1(t):
    for i in range(4):
        inner(t)   
        arc(t,150,90)
        t.lt(30)

#graph 2
def oval(t):
        t.lt(50)
        arc(t,100,80)
        t.lt(100)
        arc(t,100,80)
        t.lt(50)

def graph2(t):
    for i in range(6):
        oval(t)
        arc(t,130,60)

#graph 3
def sc(t):
    t.pendown()
    circle(t,20)

def graph3(t):
    circle(t,120)
    t.penup()
    arc(t,60,180)
    t.pendown()
    arc(t,60,180)
    t.penup()
    t.goto(00.00,120.00) 
    t.pendown()
    arc(t,60,180)  
    t.penup()
    t.goto(00.00,75.00)
    sc(t)
    t.penup()
    t.goto(00.00,195)
    sc(t)


Jason=turtle.Turtle()
graph1(Jason)
graph2(Jason)
graph3(Jason)





turtle.mainloop()

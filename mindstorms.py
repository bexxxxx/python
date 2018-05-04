##!python2

import turtle

def draw_square(some_turtle):
    for i in range(1,5):
           some_turtle.forward(100)
           some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(0,3):
        some_turtle.forward(100)
        some_turtle.left(120)

def write_initials(some_turtle):
        some_turtle.pu()
        some_turtle.setpos(-50,0)
        some_turtle.pd()
        some_turtle.left(90)
        some_turtle.forward(100)
        some_turtle.right(90)
        some_turtle.seth(0)
        some_turtle.circle(50,180)
        some_turtle.left(90)
        some_turtle.forward(100)
        some_turtle.setpos(0,0)
        
        some_turtle.pu()
        some_turtle.setpos(50,0)
        some_turtle.pd()
        some_turtle.left(180)
        some_turtle.forward(100)
        some_turtle.right(90)
        some_turtle.seth(0)
        some_turtle.circle(50,180)
        some_turtle.left(90)
        some_turtle.forward(100)
        some_turtle.setpos(100,0)
        
def draw_rhombus(some_turtle):
    for i in range(1,3):
        some_turtle.forward(80)
        some_turtle.left(40)
        some_turtle.forward(80)
        some_turtle.left(140)

def flower(some_turtle):
    for i in range(1,37):
        draw_rhombus(some_turtle)
        some_turtle.right(10)
    some_turtle.pensize(6)
    some_turtle.right(90)
    some_turtle.pencolor("green")
    some_turtle.forward(250)
    
def turtles_draw():
    window = turtle.Screen()
    window.bgcolor("purple")
    #brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed('fast')
    brad.setpos(0,0)
    flower(brad)
    #ben add extra color layer
    ben= turtle.Turtle()
    ben.shape("turtle")
    ben.color("red")
    ben.setpos(0,0)
    for i in range(1,19):
        draw_rhombus(ben)
        ben.right(20)
    
    window.exitonclick()
    
turtles_draw()

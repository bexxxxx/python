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
        
def turtles_draw():
    window = turtle.Screen()
    window.bgcolor("purple")
    #brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white", "blue")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #ben
    ben = turtle.Turtle()
    ben.shape("turtle")
    ben.color("black", "white")
    ben.circle(100)
    #brittany
    brittany = turtle.Turtle()
    brittany.shape("turtle")
    brittany.color("white", "red")
    draw_triangle(brittany)
        
    window.exitonclick()
    
turtles_draw()

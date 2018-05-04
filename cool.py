#!python2

from turtle import Turtle

#makes a spiral
t=Turtle()
t.shape("turtle")
t.speed('normal')
t.screen.bgcolor("black")
colors=["blue","purple","red","yellow","orange","brown"]
 
for x in range(300):
    t.color(colors[x%6])
    t.forward(x)
    t.left(59)
 
t.screen.exitonclick()


# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:23:54 2020

@author: 6041476
"""


import turtle as tr
tr.bgcolor("black") # change the background color
tr.textinput() # ask user for a text input
tr.numinput() # ask user for a number
tr.clearscreen() # clean screen
tr.clear() # bring turtle back to original position

t = tr.Pen() # initializes the pen you will use for drawing
t.pencolor("red") # change the pen color
t.circle(50) # makes a circle
t.left(10)
t.right(10)
t.forward(10)
t.backward(10)
t.penup() # lift your pen ... you will not be drawing
t.pendown() # bring your pen back down
t.width(10) # The thickness of your lines
t.write("Aroon") #writes stuff
t.position() #tell you where the current position of the turtle is
t.setpos(20,20)
t.heading() # gives you the direction where the turtle is pointing
t.setheading(0) # 0 = east, 90 = north, 180 = west, 270 = south
t.fillcolor("yellow")
t.begin_fill()
t.end_fill()
t.goto() # go to specific position
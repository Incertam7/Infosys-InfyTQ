Write a program to create the following pattern:
(pattern is a rectangle with a circle inside it)



import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
wn.setup(540,508)           # set window dimension

alex = turtle.Turtle()      # create a turtle named alex
alex.shape("turtle")        # alex looks like a turtle
alex.color('red')           # alex has a color

'''
alex.circle(50)              # draws a circle of radius 50
alex.backward(50)            # alex moves 50 positions backward
alex.forward(50)             # alex moves 50 positions forward
alex.right(60)               # alex turns 60 degrees right
alex.left(60)                # alex turns 60 degrees left
'''

#Write the logic to draw the given pattern
#Refer the statements given above to draw the pattern
alex.circle(50)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(200)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)

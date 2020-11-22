#Enhan Zhao 11097118

import turtle as turtle
import makedragon as dragonsegg
import random as random


def draw(dragon, x, y, segsize, heading):
    """
    Given a string describing a dragon, use Turtle graphics to
    draw its shape.
    :param dragon:  A string that describes the shape ofthe dragon.
    :param x, y: the Turtle coordinates to start drawing the dragon
    :param segsize: How big each segment of the dragon is, in Turtle pixels.
    :param heading: the orientation of the first segment of the Dragon
    :return: None
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.setheading(heading)


    

    if dragon [1] == "L":
        turtle.lt(90)
        
    else:
        turtle.rt(90)

    for i in range(2, len(dragon)):
        if dragon[i] == "L":
            turtle.lt(90)
            if dragon [i] != dragon [i - 2]:
                turtle.pencolor (random.random (), random.random (), random.random ())
            else: pass
        elif dragon[i] == "R":
            turtle.rt(90)
            if dragon [i] != dragon [i - 2]:
                turtle.pencolor (random.random (), random.random (), random.random ())
            else: pass
        else:
            turtle.fd(50)
        
            
turtle.delay(0)
turtle.speed(0)
turtle.hideturtle()

level = 4 

dragon_size = 50

segment_size = dragon_size / (2 ** (level / 2))

turtle.pensize(25 // level)

heading = 45 * (level - 1)

my_dragon = dragonsegg.dragon(level)

draw(my_dragon, -140, 140, segment_size, heading)

turtle.done()

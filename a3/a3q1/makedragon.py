# CMPT 141: Assignment 3
# This module consists of a single function,
# whose purpose is to create a string from which we can
# draw a dragon.
#
# A dragon curve is defined here to consist of 3 characters:
#    'F'  means to draw a straight line of a constant size
#    'R'  means to make a 90 degree turn to the Right (clockwise)
#    'L'  means to make a 90 degree turn to the Left (counter-clockwise)
#
# Dragon curves have many interesting properties.
#
# The function here is recursive.  That's Chapter 16.
# Don't worry if you don't understand what it is doing!

def dragon(lev):
    """
    Produces the DNA for a dragon of level lev.
    :param lev: the level of the dragon
    :return: a string that describes the dragon.
    """
    if lev == 0:
        return 'F'
    else:
        # produce DNA for a smaller dragon
        d = dragon(lev-1)
        # make a copy, reverse it, and swap the "L" and "R"
        rd = d[::-1].replace('R','T').replace('L','R').replace('T','L')
        # construct the DNA from the two , joining them with an "R"
        return d+'R'+rd




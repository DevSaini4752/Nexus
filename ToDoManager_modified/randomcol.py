"""This module will just give random color from a specific theme"""

#Importing modules
import colours as c
import random

#Func For giving random color
def col():
    #Color options
    options = [c.Hot_Pink, c.Electric_Blue, c.Orange, c.Mint_Green]
    random.shuffle(options)

    # This will give random color which will be good for CLI
    color = random.choice(options)

    return color

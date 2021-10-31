# Project 5 feature 2 provides to do list with tutrle graphic of deathstar plans.
# This program asks for the user's name and greets them.
# If the user is "Obiwan", they are asked to fight the empire!
# Otherwise they are asked to deliver the droid to Obiwan.

# import module
from turtle import *

# Get user name
name = input("Tell me your name:")


def my_function():
    # Print user greeting
    while name == "Obiwan":
        break
    else:
        print(f'Hello {name}')


def jedi_request(name):
    if name == "Obiwan":
        # If user is Obiwan help is requested
        print(f' {name}-Kenobi To do list:\n 1.Tell Luke Leia is his sister \n 2. Vader is his father\n 3. Blow up '
              f'Death Star')
        # Prints deathstar plans
        # set line color to red
        color('red')
        # draw a circle with radius of 50 pixels
        circle(150)
        # end the drawing
        color('black')
        circle(50)
        done()
    else:
        # If user is not Obiwan help is requested
        print(f'{name} \n This is not the droid you are looking for! \n please return this droid to Obiwan-Kenobi!  ')


if __name__ == '__main__':
    # Run file
    my_function()
    jedi_request(name)

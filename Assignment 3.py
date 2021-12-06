# Assignment 3
# This program takes the user's input to in a function that displays text art and
# or implements a random coin toss feature
import random

start = 0
print("Welcome to the ascii art and coin flip machine")
start = int(input("Please enter 1 to display a picture or 2 for a random coin flip: "))

def a3_function(start):
    while start > 0:
        if start ==1:
            print("You have chosen to print ascii art"  )
            a3_print()
            start = 0
        else:
            print("You have chosen flip a coin")
            a3_flip()
            start = 0

textArt = ([['.', '.', '.', '.', '.', '.'],
           ['.', 'O', 'O', '.', '.', '.'],
           ['O', 'O', 'O', 'O', '.', '.'],
           ['O', 'O', 'O', 'O', 'O', '.'],
           ['.', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', '.'],
           ['O', 'O', 'O', 'O', '.', '.'],
           ['.', 'O', 'O', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.']])
def a3_print():
    for y in range(0,6):
        for x in range(0, 9):
            if x==8:
                print(textArt[x][y])
                break
            print(textArt[x][y], end="")

def a3_flip():
    choose = input("Pick heads or tails: ")
    guess = choose
    flip = random.randint(0,1)
    if flip == 0:
        coin="heads"
    else:
        coin="tails"

    print("You picked",guess, "and the winner is",coin,"!")

a3_function(start)
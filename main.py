# Project 6! String 1
# This program reminds Obiwan what he needs to do
# If the user is not Obiwan they are asked to return the droids to him
# Asks user to input a new reminder list*** WIP currently causes droids to explode!
import sys

jedi = sys.argv

reminders = "\n 1. These are your droids\n 2. Luke and Leia are siblings,Vader is their father\n 3. Buy blue milk"
def droid_check():
    # Remind Obiwan what he needs to do
    if jedi == ['main.py', 'Obiwan']:
        print(reminders)
    # If the user is not Obiwan then instruct them to return his droids
    else:
        print(f'Hello {jedi} \n These are not the droids you are looking for! \n Return them to Obiwan-Kenobi!')

def new_to_do():
    check = input("Would you like to create a new to do list?")
    if check != "y":
        print("May the force be with you")
    else:
        remind1 = input("What do you need to remember?")
        remind1 = remind1.swapcase()
        print("~Translating to droid~"*10)
        print(remind1*5,end="\nWARNING!\nDroid malfunction!\nFatal error!!\nSelf destruct imminent!!!!\nbeeEEoupp")


# Run file
if __name__ == '__main__':
    droid_check()
    new_to_do()

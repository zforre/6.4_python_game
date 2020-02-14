import random
import time
from colorama import *
init()


def enter(player):
    # Setup
    yes_no = ["yes", "no"]
    directions = ["left", "right", "middle", "exit"]

    # Introduction
    print("You walk in the door you see a Demon standing the middle of the room")
    time.sleep(2)
    print("He looks at you and says")
    time.sleep(2)
    print(Fore.RED + "Welcome to the Thunder Dome")
    time.sleep(2)
    print(Fore.RED + ".")
    time.sleep(2)
    print(Fore.RED + ".")
    time.sleep(2)
    print(Fore.RED + ".")
    time.sleep(2)
    print(Fore.RED + "Person")
    time.sleep(2)
    print(Fore.RED + "If you wish to make it through")
    time.sleep(2)
    print(Fore.RED + "You must shred")
    time.sleep(2)
    print(Fore.RED + "BEFORE I SHRED YOU")
    time.sleep(2)
    print(".................")
    time.sleep(2)
    print(Fore.WHITE + "All of a sudden you see a light shining table")
    time.sleep(2)


    # Start of game
    response = ""
    while response not in yes_no:
        response = input("Would you like to walk to the table?\nyes/no\n")
        if response == "yes":
            print( "On the table you see three items.\n")
            time.sleep(2)
        elif response == "no":
            print(Fore.RED + "Get Rickety wRecked")
            quit()
        else:
            print("I didn't understand that.\n")
            pass
    # Next part of game
    response = ""

    while response not in directions:
        print(Fore.YELLOW + "On the LEFT side of the table you see a CHEESE GRATER.")
        time.sleep(2)
        print("On the RIGHT side of the table you see a PAPER SHREDDER.")
        time.sleep(2)
        print("And in MIDDLE of the two there is a 1970 GIBSON FLYING V.")
        time.sleep(2)
        print("Behind you is the exit.\n")
        time.sleep(2)
        response = input(Fore.WHITE + "What are you going to shred with?\nleft/right/middle/exit\n")
        time.sleep(2)
        if response == "left":
            print(Fore.RED + "The demon uses the chesse grater to add you to his pizza.")
            time.sleep(2)
            quit()
        elif response == "right":
            print(Fore.RED + "You go head first into the paper shredder.\n")
            time.sleep(2)
            quit()
        elif response == "middle":
            print(Fore.CYAN + "You pick up the Flying V your fingers start moving on their own.")
            time.sleep(1)
            print("You play the most amazing guitar solo ever played in the history of the known universe.")
            time.sleep(1)
            print("It's so beautiful the demon starts crying like a little baby.")
            time.sleep(2)
        elif response == "exit":
            print(Fore.RED + "FOOLISH HUMAN THERE IS NO ESCAPE")
            time.sleep(1)
            quit()
        else:
            print("I didn't understand that.\n")

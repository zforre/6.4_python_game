import time, m
from colorama import *
init()

# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "middle", "backward"]
play_game = True

def start():
    # Introduction
    print(Fore.GREEN + "Hey Wake up")
    time.sleep(1)
    print("......")
    time.sleep(1)
    print("Wake Up")
    print("......")
    time.sleep(2)
    print("Wake Up!!")
    time.sleep(2)
    print(Fore.WHITE + "You wake up in a cold sweat you hear a voice calling out to you.")
    time.sleep(3)
    print(Fore.GREEN + "Are you ok? I've heard the beacon I'm going to help you get home. Do you see anyone else with you?")
    print(Fore.WHITE + "You look around. You don't recgonize where you are")
    time.sleep(4)
    print("All you see is that you were chained to a bed, But somehow the chains have been cut")
    time.sleep(4)
    print("You notice other empty beds around you")
    time.sleep(4)
    print("You hear the voice again")
    time.sleep(4)
    name = input(Fore.GREEN + "What is your name?\n")
    print(Fore.GREEN + "Alright, " + name + ". Get up we don't have much time before they get here")
    print(Fore.WHITE + "You don't move")
    time.sleep(4)
    print(Fore.GREEN + "Listen " + name + " I know  all this must seem really really strange to you")
    print(F"But if you want to get back home I'm all you got chief")
    time.sleep(4)
    print(Fore.WHITE + "You get up and start walking towards an exit")
    time.sleep(4)
    print(Fore.WHITE + "Once you leave the room you see a long hallway")

    response = ""
    while response not in yes_no:
        response = input(Fore.WHITE + "Would you like to go in the hallway?\nyes/no\n")
        if response == "yes":
            print("It looks like a hotel you notice a distrubing amount of medical equipment scattered through out")
            print("Something catches your eye you walk towards the end of the hallway")
            time.sleep(3)
        elif response == "no":
            print("Your vison goes blurry you have trouble breathing.")
            time.sleep(3)
            print("You start to black out")
            time.sleep(3)
            print("A manical voice pierces through your head")
            time.sleep(3)
            print("Too late " + name + " ")
            quit()
        else:
            print("I didn't understand that.\n")

    # Next part of game
    response = ""
    while response not in directions:
        print("You notice three doors at the end of the hallway")
        time.sleep(2)
        print("To your right, you see a door.")
        time.sleep(1)
        print("There is a door in the middle.")
        time.sleep(1)
        print("To your left, you see another door.")
        time.sleep(1)
        print("Behind you is the exit.\n")

        time.sleep(1)
        response = input("What direction do you move?\nleft/right/middle/backward\n")

        if response == "left":
            print(", " + name + ".")
            quit()
        elif response == "right":
            print(".\n")
        elif response == "middle":
            print(".\n")
            m.enter()
            print('You are teleported back to the main hallway')
            time.sleep(5)
            print('You notice the middle door has vanished')
            time.sleep(4)
            print('You hear the voice comeback')
            time.sleep(4)
            print(Fore.GREEN + 'You Mad Lad you actually did it you beat NephoNecroBapho')
            time.sleep(4)
            print(Fore.GREEN + "Your not in the clear yet " + name + " there are still two more doors")
            time.sleep(4)
        elif response == "left":
                print(".\n")
        elif response == "backward":
            print("There is no escape. YOUR SOUL IS MINE, " + name + ".")
            quit()
        else:
            print("I didn't understand that.\n")

    response = input(Fore.WHITE + "What direction do you move?\nleft/right/backward\n")


while play_game:
    start()
    play_again = input('Do you want to play again?')
    if play_again == 'no':
        play_game = False

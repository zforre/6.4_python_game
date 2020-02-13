import time


# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "middle", "backward"]

# Introduction
print("Hey Wake up")
time.sleep(1)
print("......")
time.sleep(1)
print("Wake Up")
print("......")
time.sleep(3)
print("Wake Up!!")
time.sleep(2)
print("You wake up in a cold sweat you hear a voice calling out to you.")
time.sleep(5)
print("Are you ok? I've heard the beacon I'm going to help you get home. Do you see anyone else with you?")
print("You look around. You don't recgonize where you are")
time.sleep(7)
print("All you see is that you were chained to a bed, But somehow the chains have been cut")
print("You notice other empty beds around you")
print("You hear the voice again")
time.sleep(2)
name = input("What is your name?\n")
print("Alright, " + name + ". Get up we don't have much time before they get here")
print("You don't move")
time.sleep(1)
print("Listen " + name + " I know  all this must seem really really strange to you")
print("But if you want to get back home I'm all you got chief")
print("You get up and start walking towards an exit")
print("Once you leave the room you see a long hallway")

response = ""
while response not in yes_no:
    response = input("Would you like to go in the hallway?\nyes/no\n")
    if response == "yes":
        print("It looks like a hotel you notice a distrubing amount of medical equipment scattered through out")
        print("At the end of the hallway you see")

    elif response == "no":
        print("Your vison goes blurry you have trouble breathing.")
        print("You start to black out")
        print("A manical voice pierces through your head")
        print("Too late " + name + " ")
        quit()
    else:
        print("I didn't understand that.\n")

# Next part of game
response = ""
while response not in directions:
    print("You see three doors at the end of the hallway")
    time.sleep(1)
    print("To your right, you see another door.")
    time.sleep(1)
    print("There is a door in the middle.")
    time.sleep(1)
    print("To your left, you see another door.")
    time.sleep(1)
    print("Behind you is the exit.\n")
    time.sleep(1)
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print(", " + name + ".")
        quit()
    elif response == "right":
        print(".\n")
    elif response == "middle":
        print(".\n")
        response = ""
    elif response == "left":
            print(".\n")
    elif response == "backward":
        print("There is no escape. YOUR SOUL IS MINE, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")

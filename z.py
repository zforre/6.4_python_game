import time

yes_no = ["yes", "no"]
directions = ["left", "right", "middle", "exit"]

def room():
    print('You open the door farthest to the right, and take a step inside.')
    time.sleep(3)
    print('The room is empty, dark, and seems to be very small.')
    print('You notice a small table to the right of the entry, its too dark to see whats on it.')
    
    response = ""
    while response not in yes_no:
        response = input("Would you like to see what you can find on the table?\nyes/no\n")
        if response == "yes":
            print("You feel a small metal object. It's a lighter, you pick it up try to ignite it. It doesn't work the first time, or the second, but finally on the third try it works!\n")
            time.sleep(2)
        elif response == "no":
            print("You shouldn't do that, there may be something important to your survival.")
            quit()
        else:
            print("I didn't understand that.\n")
            return

    print("Now that you can see a bit, you start to notice scratches all over the floors and walls.")
    time.sleep(2)
    print("You see that there is a bed in the corner and a mirror opposite to that.")
    time.sleep(2)
    print('You walk towards the bed and cant keep from noticing how filthy it looks.')
    time.sleep(3)

    response = ""
    while response not in yes_no:
        response = input("Would you like to take a closer look at the bed?\nyes/no\n")
        if response == "yes":
            print("You pull the blanket to the side and notice a severed hand laying in a pool of blood.\n")
            time.sleep(2)
            print("The hand seems to be holding a note, you pry it out of the tight grip of the lifeless hand.")
            time.sleep(2)
            print("The letter reads, 'Beware of the helping hand for it may lead to losing yours...")
            time.sleep(2)
            print("You look down and notice that your hands are gone, you have dropped the letter and the lighter.")
            time.sleep(2)
            print("The lighter sets the note on fire, it quickly sets the bed on fire. Your only option is to run to the door")
            print("Oh no the door knob has dissapeared, you kick and punch the door, but it doesnt budge")
            time.sleep(2)
            print("The fire rises an fills the room, the lack of oxygen causes you to pass out.")
            time.sleep(3)
            print("You Died!")
        elif response == "no":
            print("You walk over to the mirror and see nothing reflected, it's like you dont exist.")
            time.sleep(2)
            print("Everything slowly starts to fade, you feel yourself sinking into darkness...")
            quit()
        else:
            print("I didn't understand that.\n")
            return
    





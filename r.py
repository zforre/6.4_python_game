import time

##The character enters the room..
def enter():
    print('As you walk into this room, there is a floodlight pointed at the door, blinding you from the rest of the room.\n\
    It looks like there isn\'t an end. Use caution, I can\'t help in there')

def walkpast():
    print('As you walk past the light, the rest of room begins to reveal itself.')
    time.sleep(3)
    print('There\'s a crumpled paper in the corner. \n\ There is a window, but it\s frosted over.')
    print('You also notice a flashlight. An odd combination for a hotel...')
    return
##The character can choose to pick up a crumpled note
def crumpled_note():
    print('Hopefully, this note will be legible')
    time.sleep(1)
    print('It looks like a letter...')
    time.sleep(1)
    print('but..this isn\'t English..')
    print('or any language I recognize')
    return

def flashlight():
    print('You picked up the flashlight and it still works')
    time.sleep(1)
    print('Well that much is lucky..')
    time.sleep(1)
    print('Pointing the light around the room, you see nothing different but..')
    time.sleep(2)
    print('The door.. it\'s..bolted shut..? How could that even happen?')
    return

## The character can choose to turn the light off, which puts them in a dangerous situation
def lightoff():
        print('You\' are met with total darkness')
        time.sleep(1)
        print('You hear the walls creaking, until you notice that one of walls is suddenly right beside you')
        time.sleep(3)
        return

## This choice is a sudden YOU WAKE UP AND HEAR THE VOICE AGAIN aka you're forced to restart
def lighton():
    print('The room is still pitch black? You toggle the switch on and off, on and off')
    time.sleep(3)
    print('nothing...')
    time.sleep(2)
    quit()

def window():
    print('I can\'t see anything through this??')
    print('What is this place?')
    return

def door():
    print('As you walk over, you notice the floor give')
    time.sleep(1)
    print('looking down, you see a trap-door below your feet')
    time.sleep(2)
    print('this could be how I get out')
    return

def trapdoor():
    print('It\'s pitch black..')
    time.sleep(1)
    print('You yell to see if anyone hears you but it only echoes')
    return


print('As you walk into this room, there is a floodlight pointed at the door, blinding you from the rest of the room.\n\
It looks like there isn\'t an end. Use caution, I can\'t help in here')
time.sleep(5)


action = input('Select your action: Turn off the lamp? Walk around the Lamp?')

if action == 'turn off the lamp':
    lightoff()
    action = input('Do you want to turn the floodlight back on?')
    if action == 'yes':
        lighton()
    else:
        print('The room is dark, but you can see a window.')
        action = input('Do you want to check it out?')

        if action == 'yes':
            window()
            time.sleep(1)
            quit()
        else:
            print('How can we find anything here?')
            action = input('Do you want to leave the room?')

            if action == 'yes':
                quit()
            else:
                action is not 'turn off the lamp'

else:
    if action == 'walk around the lamp':
        walkpast()

        explore_room = True

        while explore_room:

            action = input('Do you want to examine the paper, flashlight, or window? (enter "paper", "flashlight", or "window")')

            if action == 'flashlight':
                flashlight()
                action = input('Do you want to take a closer look at the door? yes/no?')

                if action == 'yes':
                    door()
                    action = input('Open the trap door?')

                    if action == 'yes':
                        trapdoor()
                        action = input('Do you want to continue to the door?')

                        if action == 'yes':
                            print('....')
                            time.sleep(1)
                            print('The door... its')
                            time.sleep(1)
                            print('It\'s been opened?')
                            action = input('Do you want to leave with the flashlight? Or examine the rest of the room? (leave/stay)')

                            if action == 'leave':
                                explore_room = False
                                quit()
            elif action == 'paper':
                crumpled_note()
                action = input('Do you want to turn the paper over? or leave it be? (yes/no)')
                if action == 'yes':
                    print('There\'s Spanish on this side but hard to make out. This place isn\'t very helpful.')
                    print('The note reads "la gente es la razon porque yo solo tengo a mi mismo"')
                    action = input('Do you want to keep this paper with you?')
                        # if action == 'yes': ## this needs to add paper to the class
                else:
                    pass


            elif action == 'window':
                window()

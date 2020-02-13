import time

print('As you walk into this room, there is a floodlight pointed at the door, blinding you from the rest of the room.\n\
It looks like there isn\'t an end. Use caution, I can\'t help in here')
time.sleep(5)
action = input('Select your action: Turn off the lamp? Walk around the Lamp?')

##The character enters the room..
def enter():
    print('As you walk into this room, there is a floodlight pointed at the door, blinding you from the rest of the room.\n\
    It looks like there isn\'t an end. Use caution, I can\'t help in there')

##The character can choose to pick up a crumpled note
def crumpled_note():
    print('Hopefully, this note will be legible')

## The character can choose to turn the light off, which puts them in a dangerous situation
def lightoff():
    print('You\' are met with total darkness')
    time.sleep(1)
    print('You hear the walls creaking, until you notice that one of walls is suddenly right beside you')
    time.sleep(3)
    input('Do you want to turn the floodlight back on?')

## This choice is a sudden YOU WAKE UP AND HEAR THE VOICE AGAIN aka you're forced to restart
def lighton():
    print('The room is still pitch black? You toggle the switch on and off, on and off')
    time.sleep(3)
    print('nothing...')
    time.sleep(2)
    ##returns to beginning

import time

yes_no = ["yes", "no"]

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
            print("You shouldn't have done that")
            quit()
        else:
            print("I didn't understand that.\n")
            pass



import random
import time

print("As you walk in you see a man blindfolded standing on a platform")
time.sleep(5)
print("You hear a distorted voice")
time.sleep(4)
print("HA HA HA HA HA HA YOU FOOL")
time.sleep(4)
print("All your life you lived as if what you did had no consequences")
time.sleep(4)
print("Now you will see the weight of your actions")
time.sleep(4)
print("This mans life hangs in the balance")
time.sleep(4)

def play_again():
    answer = input('Would you like to play again? yes/no').lower()
    if answer == 'y' or answer =='yes':
        play_game()
    else:
        pass

def get_word():
    words = ("redrum", "slaughter", "murder", "escape",)
    return random.choice(words)

def play_game():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = get_word()
    letters_guessed = []
    tries = 7
    guessed = False

    print('The word contains', len(word), 'letters.')
    dashes = ' '.join('_' * len(word))
    print(dashes)
    while guessed == False and tries > 0:
        print('You have ' + str(tries) + ' tries')
        guess = input('Please enter one letter or the full word.').lower()
        #1 - user inputs a letter
        if len(guess) == 1:
            if guess not in alphabet:
                print('You have not entered a letter.')
            elif guess in letters_guessed:
                print('You have already guessed that letter before.')
            elif guess not in word:
                print('You fool, that letter is not part of the word :(')
                letters_guessed.append(guess)
                tries -=1
            elif guess in word:
                print('Lucky Guess!, that letter exists in the word!')
                letters_guessed.append(guess)
            else:
                print('No idea why we get this message, should be investigated further!')

        #2 - user inputs letters where the total number of letters =/= total number of letters in the word.
        else:
            print('The length of your guess is not the same as the length of the word we\'re looking for.')

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '-'
            print(status)

        if status == word:
            print('Well done, you saved this mans life!')
            guessed = True
        elif tries == 0:
            print('You have run out of guesses and you haven\'t guessed the word.')

    play_again()

play_game()

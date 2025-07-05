#Start guessing game 

# Import packages needed to run a random guessing game 
import random

max_guesses_setting = 'Hard'

# Create a difficulty variable which can be used to define the number of guesses permitted to guess the right number
def difficulty(y):
    if y == 'Easy':
        return 7
    elif y == 'Medium':
        return 5
    elif y == 'Hard':
        return 3
    else:
        print('not a valid difficulty')
        return 0 

# Create a variable to generate a random integer (rints)
def random_number(): 

    rints = random.randint(1,2)
    rints = int(rints)
    return rints 

# Variable that allows to guess the number through the input() function 
# to ensure that the output of the guess is an int, an extra int() is added to cast the input as one. 
def guess_input(): 
    initial_guess = input()
    return int(initial_guess)
    
# Main body of the guessing game, guesses start at 1 and then a loop will be performed. 
def guessing_game():
    guess_count = 1 
    max_guesses = difficulty(max_guesses_setting)
    target = rints = random.randint(1,2)

    while guess_count <= max_guesses:
        print('This is guess '+ str(guess_count) +' out of ' + str(difficulty(max_guesses_setting)))
        player_guess = guess_input()

        if player_guess == target:
            print('You Won')
            break
        elif guess_count == max_guesses:
            print ('No more guesses left')
        else:
            print('Try Again')
        guess_count += 1

guessing_game()



              



